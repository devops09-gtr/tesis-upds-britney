"""
static_rules.py - Linea base de reglas estaticas y umbrales fijos para contraste
Fase 2 - Tesis Britney Arratia (UPDS Tarija)
"""

class StaticRuleDetector:
    def __init__(self, deauth_threshold=15, probe_threshold=100, failed_ratio_threshold=0.40):
        self.deauth_threshold = deauth_threshold
        self.probe_threshold = probe_threshold
        self.failed_ratio_threshold = failed_ratio_threshold

    def evaluate(self, feature_vector):
        """
        Evalua una ventana de 60s contra umbrales estaticos.
        Retorna: (is_anomaly, trigger_reason)
        """
        reasons = []

        if feature_vector.get("deauth_count", 0) > self.deauth_threshold:
            reasons.append(f"Deauth Flood detectado (> {self.deauth_threshold} tramas/min)")

        if feature_vector.get("probe_req_count", 0) > self.probe_threshold:
            reasons.append(f"Probe Request Flood detectado (> {self.probe_threshold} tramas/min)")

        if (feature_vector.get("failed_conn_ratio", 0.0) > self.failed_ratio_threshold and 
                feature_vector.get("ip_conn_count", 0) > 30):
            reasons.append(f"TCP Scan/Flood detectado (Failed ratio > {self.failed_ratio_threshold})")

        is_anomaly = len(reasons) > 0
        return is_anomaly, "; ".join(reasons) if is_anomaly else "Normal"
