const state = {
    labels: [],
    altitude: [],
    velocity: [],
    signal: [],
    drift: []
};

const toFixed = (v, digits = 2) => Number(v).toFixed(digits);

const createChart = (canvasId, label, color, dataRef) => {
    const ctx = document.getElementById(canvasId).getContext("2d");
    return new Chart(ctx, {
        type: "line",
        data: {
            labels: state.labels,
            datasets: [{
                label,
                data: state[dataRef],
                borderColor: color,
                backgroundColor: color.replace("1)", "0.2)") || "rgba(59,130,246,0.2)",
                fill: true,
                tension: 0.4,
                pointRadius: 0,
                borderWidth: 2.5,
                cubicInterpolationMode: "monotone"
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: { duration: 600, easing: "easeOutQuart" },
            scales: { x: { display: false }, y: { beginAtZero: false, grid: { color: "rgba(255,255,255,0.05)" }, ticks: { color: "#c7d2ff" } } },
            plugins: { legend: { display: false } }
        }
    });
};

const altitudeChart = createChart("altitudeChart", "Altitude (km)", "rgba(56, 189, 248, 1)", "altitude");
const velocityChart = createChart("velocityChart", "Velocity (km/s)", "rgba(34, 197, 94, 1)", "velocity");
const signalChart = createChart("signalChart", "Signal Strength (%)", "rgba(239, 68, 68, 1)", "signal");
const driftChart = createChart("driftChart", "Orbital Drift (deg)", "rgba(245, 158, 11, 1)", "drift");

const updateStats = (payload) => {
    const t = payload.telemetry;
    document.getElementById("altitudeVal").innerText = `${toFixed(t.altitude,3)} km`;
    document.getElementById("velocityVal").innerText = `${toFixed(t.velocity,3)} km/s`;
    document.getElementById("signalVal").innerText = `${toFixed(t.signal_strength,2)} %`;
    document.getElementById("driftVal").innerText = `${toFixed(t.orbital_drift,3)}°`;
    document.getElementById("scoreVal").innerText = toFixed(payload.risk_score,4);
    document.getElementById("anomalyVal").innerText = payload.anomaly ? "Yes" : "No";
    document.getElementById("healthStatus").innerText = payload.risk_level;
    document.getElementById("riskLevel").innerText = payload.risk_level;
    document.getElementById("recommendedAction").innerText = payload.action;
    document.getElementById("whatHappened").innerText = payload.alert.title;
    document.getElementById("why").innerText = payload.reason;

    const riskBadge = document.getElementById("riskBadge");
    riskBadge.innerText = payload.risk_level;
    const riskClass = {
        "Low Risk": "#10b981",
        "Medium Risk": "#f59e0b",
        "High Risk": "#ef4444"
    };
    riskBadge.style.background = riskClass[payload.risk_level] || "#7c3aed";

    const alertNode = document.getElementById("alertCard");
    if (payload.alert.type === "danger") {
        alertNode.className = "alert-card alert-danger";
    } else if (payload.alert.type === "warning") {
        alertNode.className = "alert-card alert-warning";
    } else {
        alertNode.className = "alert-card alert-success";
    }
    document.getElementById("alertTitle").innerText = payload.alert.title;
    document.getElementById("alertMessage").innerText = payload.alert.message;
};

const addPoint = (payload) => {
    const d = new Date(payload.telemetry.timestamp).toLocaleTimeString();
    state.labels.push(d);
    state.altitude.push(payload.telemetry.altitude);
    state.velocity.push(payload.telemetry.velocity);
    state.signal.push(payload.telemetry.signal_strength);
    state.drift.push(payload.telemetry.orbital_drift);
    if (state.labels.length > 25) {
        state.labels.shift(); state.altitude.shift(); state.velocity.shift(); state.signal.shift(); state.drift.shift();
    }
    altitudeChart.update(); velocityChart.update(); signalChart.update(); driftChart.update();
};

const fetchTelemetry = async () => {
    try {
        const res = await fetch('/api/telemetry');
        const data = await res.json();
        addPoint(data);
        updateStats(data);
    } catch (err) {
        console.error("Fetch error", err);
    }
};

fetchTelemetry();
setInterval(fetchTelemetry, 2500);
