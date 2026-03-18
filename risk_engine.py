
def classify_risk(telemetry, is_anomaly, score):
    if not is_anomaly:
        return "Low Risk"
    if telemetry["altitude"] < 410 or telemetry["orbital_drift"] > 0.18:
        return "High Risk"
    if telemetry["signal_strength"] < 80 or telemetry["velocity"] > 8.0:
        return "Medium Risk"
    if score < -0.15:
        return "Medium Risk"
    return "High Risk"


def risk_explanation(telemetry, risk_level):
    if risk_level == "Low Risk":
        return {
            "status": "Healthy orbit, telemetry nominal",
            "reason": "Telemetry values are within expected thresholds."
        }
    if telemetry["altitude"] < 412:
        return {
            "status": "Collision Risk Detected",
            "reason": "Altitude dropped too low quickly, possible orbital decay or collision trajectory."
        }
    if telemetry["signal_strength"] < 85:
        return {
            "status": "Signal Loss Risk",
            "reason": "Signal strength has dropped, indicating potential communication failure."
        }
    if telemetry["velocity"] > 7.95:
        return {
            "status": "Debris Interaction Risk",
            "reason": "Velocity spike suggests possible debris impact or thruster anomaly."
        }
    return {
        "status": "Anomalous Behavior",
        "reason": "Satellite telemetry indicates unusual values and requires attention."
    }


def recommended_action(risk_level):
    if risk_level == "Low Risk":
        return "Continue monitoring. No immediate action needed."
    if risk_level == "Medium Risk":
        return "Perform diagnostics and prepare orbit correction maneuvers."
    return "Initiate emergency protocol and command immediate orbit adjustment."
