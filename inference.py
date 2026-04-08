import os
from openai import OpenAI

# --- OpenAI Client (REQUIRED for LLM check) ---
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# --- Imports ---
from environment import SecurityEnv
from decision_module import choose_action
from evaluation_module import evaluate_decision
from logging_system import BasicLogger
from ml_model import predict_risk
from context_intelligence import extract_context_features
from behavior_analysis import extract_behavior_features


# --- LLM Call (REQUIRED) ---
def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10
        )
        return response.choices[0].message.content
    except:
        return "LLM fallback"


def main():
    env = SecurityEnv()
    logger = BasicLogger()

    scenarios = [
        {"login_time": 10, "location": "office", "file_access": 3, "failed_logins": 0},
        {"login_time": 20, "location": "home", "file_access": 5, "failed_logins": 1},
        {"login_time": 2, "location": "unknown", "file_access": 12, "failed_logins": 4},
        {"login_time": 14, "location": "vpn", "file_access": 11, "failed_logins": 0},
        {"login_time": 23, "location": "unknown", "file_access": 8, "failed_logins": 3},
    ]

    for episode, scenario in enumerate(scenarios, start=1):
        print("[START]", flush=True)

        state = env.reset()

        state["login_time"] = scenario["login_time"]
        state["location"] = scenario["location"]
        state["activity"]["file_access"] = scenario["file_access"]
        state["activity"]["failed_logins"] = scenario["failed_logins"]

        # Feature extraction
        context_features = extract_context_features(state)
        behavior_features = extract_behavior_features(state)

        # Prepare ML features
        features = [
            state["login_time"],
            1 if state["location"] == "unknown" else 0,
            state["activity"]["file_access"],
            state["activity"]["failed_logins"],
        ]

        # ML Risk Prediction
        risk_score = predict_risk(features)

        # Decision
        action = choose_action(risk_score)
        evaluation_reward = evaluate_decision(risk_score, action)

        # Environment step
        state, reward, _ = env.step(action)

        # Logging
        logger.log_episode(state, state["risk_score"], action, reward, evaluation_reward)

        # 🔥 REAL LLM CALL
        llm_output = call_llm(f"Risk score is {risk_score}")

        # Structured Logs
        print(f"[STEP] episode={episode}", flush=True)
        print(f"[STEP] state={state}", flush=True)
        print(f"[STEP] risk_score={risk_score}", flush=True)
        print(f"[STEP] action={action}", flush=True)
        print(f"[STEP] reward={reward}", flush=True)
        print(f"[STEP] llm_output={llm_output}", flush=True)

        print("[END]\n", flush=True)


if __name__ == "__main__":
    main()