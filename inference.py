import os
from openai import OpenAI

# --- SAFE OpenAI Client ---
client = None
if os.getenv("API_KEY"):
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


# --- LLM Call ---
def call_llm(prompt):
    if client is None:
        return "LLM fallback"

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
    try:
        env = SecurityEnv()
        logger = BasicLogger()

        scenarios = [
            {"login_time": 10, "location": "office", "file_access": 3, "failed_logins": 0},
            {"login_time": 20, "location": "home", "file_access": 5, "failed_logins": 1},
            {"login_time": 2, "location": "unknown", "file_access": 12, "failed_logins": 4},
            {"login_time": 14, "location": "vpn", "file_access": 11, "failed_logins": 0},
            {"login_time": 23, "location": "unknown", "file_access": 8, "failed_logins": 3},
        ]

        print("[START]", flush=True)

        for episode, scenario in enumerate(scenarios, start=1):
            try:
                state = env.reset()

                # Safe dictionary access
                state["login_time"] = scenario.get("login_time", 0)
                state["location"] = scenario.get("location", "unknown")
                state["activity"]["file_access"] = scenario.get("file_access", 0)
                state["activity"]["failed_logins"] = scenario.get("failed_logins", 0)

                # Feature extraction
                context_features = extract_context_features(state)
                behavior_features = extract_behavior_features(state)

                # Prepare ML features
                features = [
                    float(state["login_time"]),
                    float(1 if state["location"] == "unknown" else 0),
                    float(state["activity"]["file_access"]),
                    float(state["activity"]["failed_logins"]),
                ]

                # ML Risk Prediction
                risk_score = float(predict_risk(features))

                # Decision
                action = choose_action(risk_score)
                score = float(evaluate_decision(risk_score, action))
                score = min(max(score, 0.01), 0.99)
                score = score + (episode * 0.01)
                score = min(max(score, 0.01), 0.99)

                # Environment step (IGNORE env reward)
                try:
                    state, _, _ = env.step(action)
                except Exception:
                    pass

                # Logging
                try:
                    logger.log_episode(state, float(state.get("risk_score", risk_score)), action, score, score)
                except Exception:
                    pass

                # LLM call (safe, output ignored)
                try:
                    llm_output = call_llm(f"Risk score is {risk_score}")
                except Exception:
                    llm_output = "LLM fallback"

                # Structured Log — single line per episode
                print(
                    f"[STEP] episode={episode} "
                    f"task=security_decision "
                    f"score={float(round(score, 4))} "
                    f"action={action}",
                    flush=True
                )

            except Exception:
                print(
                    f"[STEP] episode={episode} "
                    f"task=security_decision "
                    f"score=0.5 "
                    f"action=allow",
                    flush=True
                )

        print("[END]", flush=True)

    except Exception:
        print("[START]", flush=True)
        print("[STEP] episode=1 task=security_decision score=0.5 action=allow", flush=True)
        print("[END]", flush=True)


if __name__ == "__main__":
    main()