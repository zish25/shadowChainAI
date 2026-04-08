import streamlit as st
from ml_model import predict_risk
from decision_module import choose_action

st.title("🔐 ShadowChain AI Dashboard")

login_time = st.slider("Login Time", 0, 23, 9)
location = st.selectbox("Location", ["office", "home", "vpn", "unknown"])
file_access = st.slider("File Access", 0, 20, 3)
failed_logins = st.slider("Failed Logins", 0, 10, 0)

if st.button("Analyze"):
    features = [
        login_time,
        1 if location == "unknown" else 0,
        file_access,
        failed_logins,
    ]

    risk = predict_risk(features)
    action = choose_action(risk)

    st.write(f"Risk Score: {round(risk,2)}")
    st.write(f"Recommended Action: {action}")
    st.progress(risk)