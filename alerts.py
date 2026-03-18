

def build_alert(telemetry, risk_level):
    if risk_level == "Low Risk":
        return {
            "title": "All clear",
            "message": "Satellite is operating within normal ranges.",
            "type": "success"
        }
    if telemetry["altitude"] < 412:
        return {
            "title": "Collision Warning",
            "message": "Altitude drop detected. Possible collision risk with debris or atmosphere.",
            "type": "danger"
        }
    if telemetry["signal_strength"] < 85:
        return {
            "title": "Communication Failure",
            "message": "Signal degradation detected. Verify antenna alignment and uplink.",
            "type": "warning"
        }
    if telemetry["velocity"] > 7.95:
        return {
            "title": "Velocity Spike",
            "message": "Unexpected speed increase. Investigate potential thruster or debris event.",
            "type": "warning"
        }
    return {
        "title": "Anomaly Alert",
        "message": "Anomaly detected. Monitor telemetry and follow risk assessment.",
        "type": "warning"
    }
