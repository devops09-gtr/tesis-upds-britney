# GUÍA DE IMPLEMENTACIÓN Y ARQUITECTURA TÉCNICA

**Proyecto:** Prototipo de Detección de Anomalías Wi-Fi (Zeek + Isolation Forest + Respuesta)  
**Tesista:** Britney Aracelly Arratia Gonzales  
**Tutor:** Ing. Gonzalo Tarifa Rodríguez  
**Versión:** 1.0 (Noviembre 2026)

---

## 1. INTRODUCCIÓN Y ALCANCE TÉCNICO

Esta guía describe cómo implementar, configurar y operar los componentes técnicos del prototipo en el banco de pruebas emulado y aislado. La arquitectura combina la captura inalámbrica en capa 2 (tramas IEEE 802.11) con la inspección estructurada de capa 3/4 mediante Zeek, procesados conjuntamente en ventanas fijas de 60 segundos.

---

## 2. TOPOLOGÍA DEL ENTORNO DE LABORATORIO

```text
       [ BANCO DE PRUEBAS AISLADO (UPDS-TEST-LAB) ]
       
   [Nodo Atacante]              [Clientes Legítimos]
   (Generador Scapy/Aircrack)   (Laptops/VMs con tráfico web/DNS)
          │                                  │
          └─────────────┬────────────────────┘
                        │ (Canal 6 / 2.4 GHz)
                        ▼
                [PUNTO DE ACCESO]
                (AP Dedicado de Laboratorio)
                        │ (Cable Ethernet)
                        ▼
           [SWITCH DE NÚCLEO / SPAN]
            (Cisco Catalyst 3650 / L3)
                        │
       ┌────────────────┴────────────────┐
       │ (Port Mirroring / SPAN)         │ (Enrutamiento L3)
       ▼                                 ▼
[SENSOR ZEEK]                    [ROUTER / FIREWALL TEST]
(Tráfico IP: conn.log, etc.)      (iptables / Reglas de Contención)
       │                                 ▲
       └────────────────┬────────────────┘
                        │
                        ▼
           [SERVIDOR DE ANÁLISIS]
   - wifi_monitor.py (Adaptador Alfa en modo monitor)
   - feature_extractor.py (Ventanas de 60 s)
   - isolation_forest.py (Modelo entrenado)
   - responder.py (Mitigación temporal)
```

---

## 3. PASO A PASO: DESPLIEGUE Y OPERACIÓN

### 3.1 Paso 1: Puesta en Modo Monitor de la Tarjeta Wi-Fi
Para capturar tramas de gestión inalámbricas (que no cruzan el cable Ethernet):
```bash
# Identificar la interfaz inalámbrica (ej. wlan0)
iwconfig

# Detener procesos que interfieran
sudo airmon-ng check kill

# Activar modo monitor en el canal del AP (ej. canal 6)
sudo airmon-ng start wlan0 6

# Verificar que la interfaz ahora sea wlan0mon
iwconfig
```

### 3.2 Paso 2: Iniciar la Captura Pasiva de Zeek
En una terminal secundaria o proceso en segundo plano:
```bash
# Iniciar Zeek escuchando en la interfaz conectada al switch de pruebas
chmod +x src/capture/zeek_runner.sh
sudo ./src/capture/zeek_runner.sh eth1 /tmp/zeek_logs
```

### 3.3 Paso 3: Ejecución del Pipeline y Extractor de Características
El script fusiona en tiempo real los contadores de Scapy con las líneas generadas en `/tmp/zeek_logs/conn.log`:
```bash
source venv/bin/activate
python src/pipeline/feature_extractor.py
```

### 3.4 Paso 4: Entrenamiento y Calibración
1. Durante la **Fase 3** (30 días de tráfico normal), se recolectan los vectores para formar `dataset_normal_base.csv`.
2. Con ese archivo, se ejecuta el entrenamiento del modelo:
```python
from src.model.isolation_forest import NetworkAnomalyDetector
import pandas as pd

df_base = pd.read_csv("data/dataset_normal_base.csv")
detector = NetworkAnomalyDetector(n_estimators=150, contamination=0.03)
detector.fit(df_base)
detector.save("models/isolation_forest_final.joblib")
print("[+] Modelo calibrado y guardado.")
```

### 3.5 Paso 5: Prueba de Mitigación Segura
Para verificar que el responder funciona sin tirar abajo la red del laboratorio:
```bash
# Probar primero en modo simulación (dry_run=True)
python src/test_pipeline.py

# Al pasar a pruebas reales en laboratorio, activar dry_run=False en responder.py
```

---

## 4. MATRIZ DE CONFIGURACIÓN DE LOS 20 ESCENARIOS DE PRUEBA

| Grupo | ID | Nombre del Escenario | Herramienta | Parámetros de Inyección |
| :--- | :--- | :--- | :--- | :--- |
| **Reconocimiento** | ESC-01 | Escaneo Pasivo de Redes | Kismet / Scapy | Canales 1 a 11, tiempo dwell 250ms |
| | ESC-02 | Sondeo Probe Flood | aireplay-ng / Scapy | 50 a 150 probe req/s |
| | ESC-03 | Inundación de Beacon | mdk4 / Scapy | Anuncio de 30 SSIDs ficticios |
| **Disponibilidad** | ESC-04 | Desautenticación (Deauth) | aireplay-ng -0 | Ráfagas de 64 tramas deauth dirigidas |
| | ESC-05 | Desasociación Masiva | Scapy Dot11Disas | Ráfagas de 30 tramas disassoc |
| | ESC-06 | Inundación de Autenticación | mdk4 a | Ráfagas de solicitudes de autenticación |
| | ESC-07 | Inundación de Asociación | mdk4 m | 100 solicitudes de asociación concurrentes |
| **Suplantación** | ESC-08 | Rogue AP (No inventariado) | Hostapd laboratorio | AP con BSSID no registrado |
| | ESC-09 | Evil Twin (AP Gemelo) | Hostapd / Airgeddon | Mismo SSID `UPDS-TEST-LAB`, BSSID distinto |
| | ESC-10 | Ataque Karma | MANA / Wifiphisher | Respuestas probe suplantadas |
| | ESC-11 | Suplantación de MAC | macchanger | Clonación de MAC de cliente activo |
| | ESC-12 | Replay de Gestión | Scapy replay | Re-inyección de capturas previas |
| **Acceso/Cifrado** | ESC-13 | Captura 4-Way Handshake | aireplay-ng + airodump | Provocar desasociación y capturar EAPoL |
| | ESC-14 | Captura PMKID | hcxdumptool | Solicitud asociación 802.11i |
| | ESC-15 | Auditoría Contraseña Débil | hashcat (offline) | Diccionario sintético de pruebas |
| | ESC-16 | Abuso WPS | reaver simulado | Peticiones M1-M4 en AP con WPS activo |
| **Servicios IP** | ESC-17 | Agotamiento DHCP | yersinia / dhcpstarv | Solicitudes DHCP Discover con MACs ficticias |
| | ESC-18 | Servidor DHCP Rogue | dnsmasq laboratorio | Ofertas DHCP contradictorias |
| | ESC-19 | ARP Spoofing | arpspoof / ettercap | Envenenamiento de caché ARP AP-Cliente |
| | ESC-20 | Suplantación DNS | dnschef | Respuestas DNS fraudulentas en LAN |
