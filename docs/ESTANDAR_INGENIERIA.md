# ESTÁNDAR DE INGENIERÍA Y RIGOR EXPERIMENTAL

**Proyecto:** Tesis de Grado en Ingeniería en Redes y Telecomunicaciones (UPDS)  
**Tesista:** Britney Aracelly Arratia Gonzales  
**Tutor:** Ing. Gonzalo Tarifa Rodríguez  
**Versión:** 1.0 (Noviembre 2026)

---

## 1. PROPÓSITO Y FILOSOFÍA DE DESARROLLO

Este documento define las normas técnicas de ingeniería de software, arquitectura de red y control de calidad experimental que rigen el proyecto. En una tesis de ingeniería, **la reproducibilidad, la trazabilidad del código y la seguridad del entorno** son tan vitales como el documento escrito. Ningún experimento es válido si su código no es versionado o sus mediciones no pueden replicarse.

---

## 2. ESTÁNDARES DE CÓDIGO Y ARQUITECTURA (PYTHON & SCRIPTS)

### 2.1 Principios de Programación
1. **Python 3.10+ PEP 8:**
   * Usar nombres descriptivos: `snake_case` para variables y funciones (`capture_wifi_window()`), `CamelCase` para clases (`NetworkAnomalyDetector`).
   * No usar números mágicos en el código. Definir constantes en mayúsculas al inicio del módulo (`WINDOW_DURATION_SEC = 60`, `DEAUTH_TYPE = 0`).
2. **Modularidad y Desacoplamiento:**
   * La lógica de captura de paquetes (`src/capture/`) no debe depender del modelo de Machine Learning (`src/model/`).
   * El pipeline de transformación (`src/pipeline/`) es el único responsable de convertir datos crudos en la matriz de características.
3. **Manejo de Errores y Logging:**
   * Prohibido el uso de `except: pass` silencioso.
   * Usar siempre el módulo estándar `logging` con niveles apropiados:
     * `DEBUG`: Detalles de paquetes individuales.
     * `INFO`: Inicio y fin de ventanas de 60s, resumen de métricas.
     * `WARNING`: Eventos anómalos o timeouts de interfaz.
     * `ERROR` / `CRITICAL`: Pérdida de interfaz en modo monitor o fallas de escritura.

---

## 3. ESTÁNDAR DE REGISTRO EXPERIMENTAL (LOGGING DE LAS 600 CORRIDAS)

Para cumplir con la hipótesis aprobada en el perfil, cada una de las **600 ejecuciones** (20 escenarios $\times$ 30 repeticiones) debe quedar registrada de forma inmutable:

### 3.1 Estructura Obligatoria de la Ficha Experimental (`run_manifest.json`)
Cada corrida de prueba debe generar un registro JSON o CSV con los siguientes campos obligatorios:

```json
{
  "run_id": "ESC04_RUN01_20270205_143022",
  "scenario_id": 4,
  "scenario_name": "Deauthentication Flood",
  "iteration": 1,
  "timestamp_start_attack": 1738769422.124,
  "timestamp_end_attack": 1738769482.124,
  "target_mac": "02:00:00:aa:bb:01",
  "target_bssid": "00:14:d1:e2:33:44",
  "channel": 6,
  "intensity_params": {
    "rate_packets_per_sec": 50,
    "packet_type": "dot11_deauth"
  },
  "ground_truth_label": 1,
  "model_prediction": {
    "isolation_forest": {
      "predicted_label": 1,
      "anomaly_score": -0.1425,
      "timestamp_detection": 1738769438.450
    },
    "static_rules": {
      "predicted_label": 1,
      "trigger_reason": "Deauth count > 15",
      "timestamp_detection": 1738769440.010
    }
  },
  "response_action": {
    "action_executed": "iptables_drop_mac",
    "timestamp_action": 1738769441.100,
    "latency_seconds": 18.976,
    "status": "SUCCESS"
  }
}
```

---

## 4. PROTOCOLOS DE SEGURIDAD Y AISLAMIENTO DE RED (FAIL-SAFE)

1. **Aislamiento Físico y Lógico Estricto:**
   * El AP y los clientes de prueba deben operar en un SSID dedicado de laboratorio (`UPDS-TEST-LAB`).
   * La interfaz de red de administración/Internet jamás debe enrutarse hacia el segmento de ataque.
2. **Protección contra Auto-Bloqueos (Whitelist):**
   * El módulo `responder.py` debe incluir de manera rígida una lista blanca de direcciones MAC e IP:
     * MAC de la tarjeta de red del sensor.
     * MAC del switch/gateway de laboratorio.
     * IP de administración del servidor de control.
3. **Mecanismo de Desconexión de Emergencia (Kill Switch):**
   * Todo script de inyección de paquetes o respuesta automatizada debe responder a `SIGINT` (Ctrl+C) limpiando las reglas añadidas en `iptables` (`iptables -F`) y restaurando la interfaz de red a su estado original.

---

## 5. CONTROL DE VERSIONES (GIT WORKFLOW)

1. **Ramas Principales:**
   * `main`: Código estable, validado y aprobado por el Tutor.
   * `develop`: Rama de integración donde la estudiante desarrolla las fases.
2. **Ramas por Tarea (Feature Branches):**
   * Formato: `feature/fase2-sensor-wifi`, `feature/fase2-zeek-pipeline`, `fix/iptables-timeout`.
3. **Mensajes de Commit Semánticos:**
   * `feat: ...` (nueva funcionalidad).
   * `fix: ...` (corrección de bugs o errores de captura).
   * `docs: ...` (actualización de manuales o secciones de tesis).
   * `test: ...` (pruebas unitarias o experimentales).
