import random
import datetime

BASE_ALTITUDE = 420.0
BASE_VELOCITY = 7.66
BASE_SIGNAL = 98.0
BASE_DRIFT = 0.0


def generate_telemetry():
    altitude = round(BASE_ALTITUDE + random.uniform(-1.8, 1.8) + random.choice([0, 0, 0, -8, 8]), 3)
    velocity = round(BASE_VELOCITY + random.uniform(-0.04, 0.06) + random.choice([0, 0, 0.3, -0.2]), 4)
    signal_strength = round(BASE_SIGNAL + random.uniform(-2.7, 1.2) + random.choice([0, 0, -16, -8]), 2)
    orbital_drift = round(BASE_DRIFT + random.uniform(-0.06, 0.1) + random.choice([0, 0, 0.25]), 4)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    return {
        "timestamp": timestamp,
        "altitude": altitude,
        "velocity": velocity,
        "signal_strength": signal_strength,
        "orbital_drift": orbital_drift
    }
