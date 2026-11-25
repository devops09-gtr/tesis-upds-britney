"""
isolation_forest.py - Wrapper para detector no supervisado Isolation Forest
Fase 2 - Tesis Britney Arratia (UPDS Tarija)
"""

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

class NetworkAnomalyDetector:
    def __init__(self, n_estimators=150, contamination=0.03, max_samples=256, random_state=42):
        self.model = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            max_samples=max_samples,
            random_state=random_state,
            n_jobs=-1
        )
        self.is_fitted = False
        self.feature_columns = [
            "deauth_count", "disassoc_count", "beacon_count", "probe_req_count",
            "unique_macs", "ip_conn_count", "failed_conn_ratio", "total_bytes", "unique_ips"
        ]

    def fit(self, df_normal):
        """Entrena el modelo unicamente con la linea base normal (30 dias)."""
        X = df_normal[self.feature_columns]
        self.model.fit(X)
        self.is_fitted = True
        return self

    def predict(self, feature_vector):
        """
        Evalua una ventana de 60s.
        Retorna:
          is_anomaly: True (-1) o False (1)
          score: Anomaly score (valores mas bajos/negativos indican anomalia severa)
        """
        if not self.is_fitted:
            raise RuntimeError("El modelo debe ser entrenado antes de predecir.")

        if isinstance(feature_vector, dict):
            df = pd.DataFrame([feature_vector])[self.feature_columns]
        elif isinstance(feature_vector, pd.DataFrame):
            df = feature_vector[self.feature_columns]
        else:
            df = pd.DataFrame(feature_vector, columns=self.feature_columns)

        pred = self.model.predict(df)[0]
        score = self.model.decision_function(df)[0]

        is_anomaly = (pred == -1)
        return is_anomaly, score

    def save(self, filepath):
        joblib.dump({"model": self.model, "columns": self.feature_columns}, filepath)

    def load(self, filepath):
        data = joblib.load(filepath)
        self.model = data["model"]
        self.feature_columns = data["columns"]
        self.is_fitted = True
