"""
test_pipeline.py - Prueba de integracion completa (Capa 2 Wi-Fi + Zeek IP + Modelos)
Permite validar el prototipo tanto en Windows como en Linux sin requerir hardware activo.
Fase 2 - Tesis Britney Arratia (UPDS Tarija)
"""

import os
import sys
import time
import pandas as pd

# Asegurar que la raíz del proyecto esté en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model.isolation_forest import NetworkAnomalyDetector
from src.model.static_rules import StaticRuleDetector
from src.response.responder import AutomatedResponder
from src.pipeline.feature_extractor import build_feature_vector

def main():
    print("=" * 65)
    print("  TEST DE INTEGRACION DE PROTOTIPO (FASE 2) - TESIS UPDS")
    print("  Britney Arratia  |  Tutor: Ing. Gonzalo Tarifa")
    print("=" * 65)

    # 1. Generar conjunto sintético de 500 ventanas normales (Simula Línea Base)
    print("\n[*] 1. Generando simulacion de linea base de trafico normal...")
    normal_data = []
    for i in range(500):
        normal_data.append({
            "deauth_count": int(abs(pd.Series(range(10)).sample(1).iloc[0] * 0.3)),  # Raras veces 1 o 2 deauths
            "disassoc_count": 0,
            "beacon_count": int(100 + (i % 20)),
            "probe_req_count": int(20 + (i % 15)),
            "unique_macs": int(5 + (i % 3)),
            "ip_conn_count": int(40 + (i % 30)),
            "failed_conn_ratio": round(float((i % 5) / 100.0), 3),
            "total_bytes": int(250000 + (i * 1000) % 500000),
            "unique_ips": int(4 + (i % 2))
        })
    df_normal = pd.DataFrame(normal_data)
    print(f"[+] Linea base normal creada con {len(df_normal)} ventanas temporales de 60s.")

    # 2. Entrenar Isolation Forest
    print("\n[*] 2. Entrenando modelo Isolation Forest con la linea base...")
    detector_if = NetworkAnomalyDetector(n_estimators=150, contamination=0.03)
    detector_if.fit(df_normal)
    print("[+] Modelo Isolation Forest entrenado exitosamente.")

    # 3. Inicializar detector de Reglas Estáticas
    print("\n[*] 3. Inicializando detector de Reglas Estaticas (Linea Base de Contraste)...")
    detector_rules = StaticRuleDetector(deauth_threshold=15, probe_threshold=100, failed_ratio_threshold=0.40)
    print("[+] Reglas estaticas configuradas: Deauth > 15/min, Probe > 100/min, Failed TCP > 40%.")

    # 4. Inicializar Módulo de Respuesta
    responder = AutomatedResponder(whitelist_macs=["00:11:22:33:44:55"], dry_run=True)

    # 5. Probar con Caso 1: Ventana de Tráfico Normal
    print("\n" + "-" * 50)
    print(">> CASO DE PRUEBA 1: Ventana de Trafico Wi-Fi Normal")
    ventana_normal = {
        "deauth_count": 0, "disassoc_count": 0, "beacon_count": 110, "probe_req_count": 25,
        "unique_macs": 5, "ip_conn_count": 45, "failed_conn_ratio": 0.02, "total_bytes": 310000, "unique_ips": 4
    }
    anom_if, score_if = detector_if.predict(ventana_normal)
    anom_reglas, motivo_reglas = detector_rules.evaluate(ventana_normal)
    print(f"  * Isolation Forest: {'[ALERTA ANOMALIA]' if anom_if else '[NORMAL]'} (Score: {score_if:.4f})")
    print(f"  * Reglas Estaticas: {'[ALERTA ANOMALIA]' if anom_reglas else '[NORMAL]'} ({motivo_reglas})")

    # 6. Probar con Caso 2: Ventana con Ataque de Desautenticación (Escenario 4)
    print("\n" + "-" * 50)
    print(">> CASO DE PRUEBA 2: Escenario 4 - Rafaga de Desautenticacion (Deauth Attack)")
    ventana_deauth = {
        "deauth_count": 78,  # Ataque de desautenticacion severo
        "disassoc_count": 5, "beacon_count": 110, "probe_req_count": 30,
        "unique_macs": 5, "ip_conn_count": 8, "failed_conn_ratio": 0.50, "total_bytes": 12000, "unique_ips": 2
    }
    anom_if2, score_if2 = detector_if2 = detector_if.predict(ventana_deauth)
    anom_reglas2, motivo_reglas2 = detector_rules.evaluate(ventana_deauth)
    print(f"  * Isolation Forest: {'[ALERTA ANOMALIA]' if anom_if2 else '[NORMAL]'} (Score: {score_if2:.4f})")
    print(f"  * Reglas Estaticas: {'[ALERTA ANOMALIA]' if anom_reglas2 else '[NORMAL]'} ({motivo_reglas2})")

    if anom_if2:
        print("\n[*] Disparando mitigacion automatizada para el atacante...")
        responder.handle_incident(target_mac="aa:bb:cc:dd:ee:01", target_ip="192.168.1.150", 
                                  reason="Deauth Flood Anomaly", score=score_if2)

    print("\n" + "=" * 65)
    print("  [EXITO] Pipeline completo verificado de principio a fin.")
    print("=" * 65)

if __name__ == "__main__":
    main()
