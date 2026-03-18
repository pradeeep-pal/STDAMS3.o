import numpy as np
from sklearn.ensemble import IsolationForest
from simulator import generate_telemetry

class IsolationForestModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.08, random_state=42)
        self.is_trained = False

    def _to_feature(self, telemetry):
        return [telemetry["altitude"], telemetry["velocity"], telemetry["signal_strength"], telemetry["orbital_drift"]]

    def train_initial(self, n=250):
        X = [self._to_feature(generate_telemetry()) for _ in range(n)]
        self.model.fit(X)
        self.is_trained = True

    def predict_anomaly(self, telemetry):
        if not self.is_trained:
            self.train_initial()
        features = np.array([self._to_feature(telemetry)])
        pred = self.model.predict(features)[0]
        return bool(pred == -1)

    def predict_score(self, telemetry):
        features = np.array([self._to_feature(telemetry)])
        score = self.model.decision_function(features)[0]
        return float(score)
