from environment import SecurityEnv
from behavior_analysis import extract_behavior_features
from context_intelligence import extract_context_features
from decision_module import choose_action
from evaluation_module import evaluate_decision
from logging_system import BasicLogger
from risk_engine import calculate_risk_score


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
        state = env.reset()

        state["login_time"] = scenario["login_time"]
        state["location"] = scenario["location"]
        state["activity"]["file_access"] = scenario["file_access"]
        state["activity"]["failed_logins"] = scenario["failed_logins"]

        context_features = extract_context_features(state)
        behavior_features = extract_behavior_features(state)
        risk_score = calculate_risk_score(context_features, behavior_features)
        action = choose_action(risk_score)
        evaluation_reward = evaluate_decision(risk_score, action)

        state, reward, _ = env.step(action)

        logger.log_episode(state, state["risk_score"], action, reward, evaluation_reward)

        print(f"=== Episode {episode} ===")
        print(f"state: {state}")
        print(f"risk_score: {state['risk_score']}")
        print(f"chosen action: {action}")
        print(f"reward: {reward}\n")


if __name__ == "__main__":
    main()
