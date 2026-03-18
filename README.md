# Satellite Risk Monitoring & Alert System (SRMAS)

A lightweight Flask project that simulates satellite telemetry, uses Isolation Forest anomaly detection, and displays a modern dashboard with live charts, risk classification, and recommended actions.

## Features

- Simulated satellite telemetry (altitude, velocity, signal strength, orbital drift)
- Anomaly detection with Isolation Forest
- Risk classification: Low, Medium, High
- Live Chart.js animated telemetry graphs
- Professional dashboard with color-coded risk and alerts

## Project Files

- `app.py`: Flask backend API and dashboard route
- `simulator.py`: Simulated telemetry generator
- `anomaly_model.py`: Isolation Forest model and predictions
- `risk_engine.py`: Risk classification and explanation
- `alerts.py`: Alert card generation
- `templates/dashboard.html`: Dashboard UI
- `static/style.css`: Dashboard styling
- `static/script.js`: Live update logic and charts

## Run

1. Create virtualenv
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies
   ```bash
   pip install flask scikit-learn
   ```
3. Run server
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000`

## How it works

- `/api/telemetry` returns simulated telemetry with anomaly/risk classification.
- Client polls every 2.5s to update charts and risk panel.
- Risk panel explains what happened, why, and recommended action.
