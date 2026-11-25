"""
feature_extractor.py - Fusiona tramas Wi-Fi de capa 2 y registros IP de Zeek en ventanas de 60 s
Fase 2 - Tesis Britney Arratia (UPDS Tarija)
"""

import os
import json
import pandas as pd

def parse_zeek_conn_log(conn_log_path, window_start, window_end):
    """
    Parsea registros conn.log de Zeek correspondientes al intervalo temporal.
    Zeek conn.log fields comunes: ts, id.orig_h, id.resp_h, id.resp_p, proto, orig_bytes, resp_bytes, conn_state
    """
    if not os.path.exists(conn_log_path):
        return {
            "ip_conn_count": 0,
            "failed_conn_ratio": 0.0,
            "total_bytes": 0,
            "unique_ips": 0
        }

    connections = []
    try:
        with open(conn_log_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                parts = line.strip().split("\t")
                if len(parts) >= 12:
                    ts = float(parts[0])
                    if window_start <= ts <= window_end:
                        conn_state = parts[11]  # ej. S0, SF, REJ
                        orig_bytes = int(parts[9]) if parts[9] != "-" else 0
                        resp_bytes = int(parts[10]) if parts[10] != "-" else 0
                        connections.append({
                            "ts": ts,
                            "orig_ip": parts[2],
                            "resp_ip": parts[4],
                            "state": conn_state,
                            "bytes": orig_bytes + resp_bytes
                        })
    except Exception as e:
        print(f"[!] Error leyendo zeek log: {e}")

    if not connections:
        return {
            "ip_conn_count": 0,
            "failed_conn_ratio": 0.0,
            "total_bytes": 0,
            "unique_ips": 0
        }

    df = pd.DataFrame(connections)
    total_conn = len(df)
    failed_conn = len(df[df["state"].isin(["S0", "REJ", "RSTO", "RSTR"])])
    failed_ratio = failed_conn / total_conn if total_conn > 0 else 0.0
    total_bytes = df["bytes"].sum()
    unique_ips = len(set(df["orig_ip"]).union(set(df["resp_ip"])))

    return {
        "ip_conn_count": total_conn,
        "failed_conn_ratio": round(failed_ratio, 4),
        "total_bytes": int(total_bytes),
        "unique_ips": unique_ips
    }

def build_feature_vector(wifi_metrics, zeek_metrics):
    """Fusiona las caracteristicas de ambas fuentes en un único diccionario para el modelo."""
    vector = {
        # Caracteristicas Capa 2 (Wi-Fi 802.11)
        "deauth_count": wifi_metrics.get("deauth_count", 0),
        "disassoc_count": wifi_metrics.get("disassoc_count", 0),
        "beacon_count": wifi_metrics.get("beacon_count", 0),
        "probe_req_count": wifi_metrics.get("probe_req_count", 0),
        "unique_macs": wifi_metrics.get("unique_macs", 0),
        
        # Caracteristicas Capa 3/4 (Zeek IP)
        "ip_conn_count": zeek_metrics.get("ip_conn_count", 0),
        "failed_conn_ratio": zeek_metrics.get("failed_conn_ratio", 0.0),
        "total_bytes": zeek_metrics.get("total_bytes", 0),
        "unique_ips": zeek_metrics.get("unique_ips", 0)
    }
    return vector

if __name__ == "__main__":
    # Test sintético de integración
    mock_wifi = {"deauth_count": 3, "disassoc_count": 0, "beacon_count": 120, "probe_req_count": 15, "unique_macs": 4}
    mock_zeek = {"ip_conn_count": 45, "failed_conn_ratio": 0.02, "total_bytes": 150420, "unique_ips": 3}
    feat = build_feature_vector(mock_wifi, mock_zeek)
    print("[+] Vector fusionado de prueba:")
    print(json.dumps(feat, indent=2))
