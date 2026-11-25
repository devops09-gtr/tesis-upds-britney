# GUIA OPERATIVA: FASE 2 - IMPLEMENTACION DEL PROTOTIPO Y PIPELINE

**Fase:** Fase 2 del Cronograma de Modalidad de Grado II  
**Objetivo:** Desplegar el AP, sensor inalambrico en modo monitor, analizador Zeek, pipeline de fusion por ventanas temporales y scripts de mitigacion automatizada.  
**Entregable vinculado:** 1.er Informe de Control institucional.

---

## 1. Arquitectura General del Prototipo en Fase 2

El prototipo consta de 4 subsistemas integrados:

```text
       [ Medio Wi-Fi 802.11 ]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 [Sensor Wi-Fi]       [AP / Switch]
  (Modo Monitor)            │
        │             [Sensor Zeek]
        │              (Tráfico IP)
        ▼                   ▼
  wifi_events.csv       conn.log, dns.log
        └─────────┬─────────┘
                  ▼
      [Pipeline de Fusión] ─── (Ventana: 60 s)
                  │
                  ▼
          [Matriz de Features]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
[Isolation Forest]    [Reglas Estáticas]
        │                   │
        └─────────┬─────────┘
                  ▼
      [Módulo de Respuesta]
    (Alerta / Bloqueo Temporal)
```

---

## 2. Requisitos Previos e Instalacion de Software

### 2.1 Sistema Operativo Recomendado
* Ubuntu Linux 22.04 LTS / 24.04 LTS o Debian 12 (nativo o en maquina virtual Proxmox/VirtualBox con paso USB del adaptador Wi-Fi).

### 2.2 Paquetes del Sistema
Ejecutar en la terminal:
```bash
sudo apt update && sudo apt install -y \
    python3 python3-pip python3-venv \
    tshark tcpdump net-tools wireless-tools aircrack-ng \
    iptables iptables-persistent curl git
```

### 2.3 Instalacion de Zeek
Para instalar Zeek LTS en Ubuntu/Debian:
```bash
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' > /etc/apt/sources.list.d/security:zeek.list"
curl -fsSL https://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
sudo apt update
sudo apt install -y zeek-lts
export PATH=$PATH:/opt/zeek/bin
```

### 2.4 Instalacion de Librerias Python
Dentro de este repositorio:
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Componentes de Codigo Desarrollados en `src/`

### 3.1 Capturador Inalambrico (`src/capture/wifi_monitor.py`)
* Configura la tarjeta inalámbrica en modo monitor (`iwconfig` / `airmon-ng`).
* Utiliza `Scapy` o `tshark` para escuchar tramas de gestion y control en el canal asignado (por ejemplo, Canal 6 o Canal 1).
* Extrae contadores en tiempo real:
  * Conteo de tramas `Beacon` por BSSID.
  * Conteo de tramas `Probe Request` y `Probe Response`.
  * Conteo de tramas de desautenticacion (`Deauth`, sub-tipo 12) y desasociacion (`Disassoc`, sub-tipo 10).
  * Conteo de intentos de autenticacion y asociacion.

### 3.2 Capturador de Trafico IP (`src/capture/zeek_runner.sh`)
* Inicia Zeek a la escucha en la interfaz de red interna conectada al switch/AP de laboratorio (`eth1` o `br0`).
* Genera los logs estructurados estándar en un directorio temporal (`/tmp/zeek_logs/`):
  * `conn.log`: Duracion, IPs origen/destino, puertos, bytes enviados/recibidos, estado TCP (`S0`, `SF`, `REJ`).
  * `dns.log`: Consultas DNS, dominios, respuestas y errores.
  * `dhcp.log`: Transacciones DHCP Discover/Offer/Request/ACK.

### 3.3 Extractor y Pipeline de Fusion (`src/pipeline/feature_extractor.py`)
* Lee las marcas de tiempo de ambas fuentes y las agrupa en **ventanas fijas de 60 segundos**.
* Genera un vector normalizado de caracteristicas por ventana:
  1. `deauth_count`: Numero de tramas de desautenticacion.
  2. `probe_req_count`: Numero de solicitudes probe.
  3. `unique_macs_seen`: Cantidad de direcciones MAC distintas detectadas.
  4. `ip_conn_count`: Numero de conexiones IP iniciadas en la ventana.
  5. `failed_conn_ratio`: Ratio de conexiones TCP no completadas (posible escaneo/flood).
  6. `total_bytes`: Volumen de datos transferidos.
  7. `dns_query_count`: Frecuencia de consultas DNS.

### 3.4 Modelo Isolation Forest (`src/model/isolation_forest.py`)
* Implementa la clase `AnomalyDetector` envolviendo `sklearn.ensemble.IsolationForest`.
* Parametros de base calibrables:
  * `n_estimators=150` (cantidad de arboles de aislamiento).
  * `contamination=0.03` (proporcion estimada de anomalias esperadas en trafico real: 3% a 5%).
  * `max_samples=256` (submuestreo eficiente para limitar el uso de CPU/RAM).
* Metodos:
  * `fit(normal_dataframe)`: Entrena exclusivamente con la linea base normal.
  * `predict(feature_window)`: Retorna `1` (normal) o `-1` (anomalo) junto con el `anomaly_score`.

### 3.5 Linea Base de Reglas Estaticas (`src/model/static_rules.py`)
* Implementa las reglas fijas de contraste acordadas en el perfil:
  * *Regla 1:* `deauth_count > 15` tramas/min ➔ Alerta Ataque Desautenticacion.
  * *Regla 2:* `probe_req_count > 100` tramas/min ➔ Alerta Escaneo Probe.
  * *Regla 3:* `failed_conn_ratio > 0.40` con `ip_conn_count > 50` ➔ Alerta Escaneo de Puertos / DoS IP.
  * *Regla 4:* Aparicion de BSSID no registrado en el inventario autorizado ➔ Alerta Rogue AP.

### 3.6 Modulo de Respuesta Automatizada (`src/response/responder.py`)
* Recibe la notificacion de anomalia del detector.
* Registra el incidente con marca de tiempo precisa en `experiments/logs/response_events.log`.
* Ejecuta accion gradual:
  1. Si la severidad es media: Registra advertencia y genera log.
  2. Si la severidad es alta (confirmacion en 2 ventanas consecutivas o score > umbral critico):
     * Aplica bloqueo temporal de 5 minutos al dispositivo mediante `iptables -I FORWARD -m mac --mac-source <MAC> -j DROP`.
     * Lista blanca de exclusion (IP/MAC del servidor de monitoreo y gateway) para prevenir auto-bloqueos.

---

## 4. Protocolo de Pruebas de la Fase 2 (Checklist de Verificacion)

Antes de pasar a la Fase 3 (captura de 30 dias), Britney debe verificar:

1. [ ] La tarjeta de red Wi-Fi se activa en modo monitor sin errores (`wlan0mon` o similar).
2. [ ] El script `wifi_monitor.py` detecta y contabiliza paquetes reales en el canal de laboratorio.
3. [ ] Zeek genera correctamente los archivos `conn.log` y `dhcp.log`.
4. [ ] El extractor de caracteristicas combina ambos origenes en ventanas de 60 s sin desfase temporal.
5. [ ] El script de mitigacion bloquea temporalmente una MAC de prueba y restaura el trafico tras el timeout.
