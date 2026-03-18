from flask import Flask, jsonify, render_template
from simulator import generate_telemetry
from anomaly_model import IsolationForestModel
from risk_engine import classify_risk, risk_explanation, recommended_action
from alerts import build_alert

app = Flask(__name__)
model = IsolationForestModel()

# Pretrain model with simulated normal points to establish baseline
model.train_initial(300)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/telemetry")
def telemetry():
    data = generate_telemetry()
    risk_score = model.predict_score(data)
    is_anomaly = model.predict_anomaly(data)
    risk_level = classify_risk(data, is_anomaly, risk_score)
    explanation = risk_explanation(data, risk_level)
    action = recommended_action(risk_level)
    alert = build_alert(data, risk_level)
    response = {
        "telemetry": data,
        "anomaly": is_anomaly,
        "risk_score": round(float(risk_score), 4),
        "risk_level": risk_level,
        "status": explanation["status"],
        "reason": explanation["reason"],
        "action": action,
        "alert": alert
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
