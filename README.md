# ShadowChainAI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-TBD-lightgrey)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

ShadowChainAI is an intelligent cybersecurity decision simulation system that models login events, predicts risk using Machine Learning, and recommends appropriate security actions through an interactive pipeline.

---

## 🌐 Overview

ShadowChainAI simulates real-world security login scenarios and applies a modular pipeline to:

* Analyze contextual and behavioral signals
* Predict risk using a Machine Learning model
* Select optimal defensive actions
* Evaluate decision effectiveness

The system combines simulation, ML-based intelligence, and interactive visualization for better cybersecurity analysis.

---

## ✨ Key Features

* 🔹 Modular pipeline: context → behavior → ML risk → decision → evaluation
* 🤖 Machine Learning-based risk prediction (Logistic Regression)
* 📊 Interactive web dashboard using Streamlit
* 🔍 Interpretable features: time, location, failed logins, file access
* ⚡ Lightweight and easy to run (minimal dependencies)
* 🧪 Scenario-based simulation for testing security events

---

## 🧠 Machine Learning Integration

We enhanced the system by replacing rule-based risk scoring with a **Logistic Regression model**.

The model learns from:

* Login time
* Location anomaly (known vs unknown)
* File access patterns
* Failed login attempts

This enables **adaptive, data-driven risk prediction** instead of static threshold-based logic.

---

## 🧩 Features

* Simulates security events (login time, location, activity)
* Extracts contextual and behavioral features
* Predicts risk using ML model
* Chooses defensive actions (`allow`, `monitor`, `block`)
* Evaluates decisions using reward signals
* Logs each episode for analysis

---

## 🗂️ Project Structure

* `environment.py` → Security simulation environment
* `context_intelligence.py` → Context feature extraction
* `behavior_analysis.py` → Behavior feature extraction
* `risk_engine.py` → (legacy rule-based system)
* `ml_model.py` → Machine Learning model for risk prediction ✅
* `decision_module.py` → Action selection logic
* `evaluation_module.py` → Decision evaluation
* `logging_system.py` → Logging system
* `inference.py` → End-to-end simulation runner
* `app.py` → Streamlit web interface ✅
* `test_env.py` → Environment testing

---

## 🛡️ Security Response Model

### ⚙️ Action Space

* `allow` → Safe activity
* `monitor` → Suspicious but not critical
* `block` → High-risk activity
* `quarantine` → Isolate system

---

## 📊 Risk Prediction (ML-Based)

Instead of static rules, risk is predicted using a trained ML model:

* Output range: **0 to 1 (probability of risk)**
* Higher value → more dangerous activity
* Used as input to decision module

---

## 🔐 Security Validation

We integrated **Semgrep** for static code analysis to ensure code safety.

* ✅ No known vulnerabilities detected
* 🔍 Secure and reliable baseline system
* 🛡️ Complements ML-based behavioral analysis

---

## 🎯 Why This Project

* Demonstrates transition from rule-based → ML-based systems
* Simulates real cybersecurity decision-making
* Provides an interpretable yet intelligent pipeline
* Combines **AI + Cybersecurity + Simulation + UI**

---

## 🧰 Setup and Requirements

### Requirements

* Python 3.9+
* Install dependencies:

```bash
pip install scikit-learn streamlit
```

---

## 🚀 How to Run

### ▶️ Run Simulation (Backend)

```bash
python inference.py
```

---

### 🌐 Run Web Interface

```bash
streamlit run app.py
```

👉 Opens interactive dashboard in browser

---

### 🧪 Run Environment Tests

```bash
python test_env.py
```

---

## 🖥️ Demo Output

```text
=== Episode 1 ===
state: {...}
risk_score: 0.72
chosen action: block
reward: 1.0
```

---

## 🔄 Example Pipeline

1. Initialize environment
2. Input scenario (time, location, activity)
3. Extract features
4. Predict risk using ML model
5. Choose action
6. Execute in environment
7. Evaluate and log results

---

## 🌐 Web Dashboard Features

* Input user login behavior
* Real-time risk prediction
* Action recommendation
* Visual risk indicator (progress bar)

---

## 🔭 Future Scope

* Replace Logistic Regression with advanced models (XGBoost, Neural Networks)
* Add anomaly detection (Isolation Forest)
* Store logs in database
* Add real-time monitoring dashboard
* Integrate with real cybersecurity datasets

---

## 📄 License

Add a license file if you plan to publish or distribute the project.

---

## 🧠 One-Line Summary

ShadowChainAI is an ML-powered cybersecurity simulation system that transforms login behavior into intelligent risk predictions and adaptive security actions.
