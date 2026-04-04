"""
ShadowChainAI - OpenEnv Security Environment
Minimal environment for cybersecurity threat simulation.
"""


class SecurityEnv:
    """OpenEnv-style environment for security operations."""

    VALID_ACTIONS = ["allow", "block", "quarantine", "monitor"]
    KNOWN_LOCATIONS = ["office", "home", "vpn"]

    def __init__(self):
        self.state = {}
        self.done = False
        self.history = []

    def reset(self):
        """Reset environment to initial state."""
        self.done = False
        self.state = {
            "login_time": 9,           # hour of day (0-23)
            "location": "office",       # office | home | vpn | unknown
            "activity": {
                "file_access": 3,       # number of files accessed
                "failed_logins": 0,     # number of failed login attempts
            },
            "risk_score": 0.0,
        }
        return self.state

    def step(self, action):
        """
        Process an action and return (state, reward, done).

        Args:
            action: one of 'allow', 'block', 'quarantine', 'monitor'

        Returns:
            tuple: (updated_state, reward, done)
        """
        if self.done:
            return self.state, 0.0, True

        if action not in self.VALID_ACTIONS:
            return self.state, -1.0, False

        # --- Risk Score Calculation ---
        risk_score = 0.0

        # Time-based risk: outside business hours (9-17) is riskier
        login_time = self.state["login_time"]
        if login_time < 6 or login_time > 22:
            risk_score += 0.4        # late night = high risk
        elif login_time < 9 or login_time > 17:
            risk_score += 0.2        # outside office hours = moderate risk

        # Location-based risk
        location = self.state["location"]
        if location not in self.KNOWN_LOCATIONS:
            risk_score += 0.3        # unknown location = risky

        # Activity-based risk
        file_access = self.state["activity"]["file_access"]
        failed_logins = self.state["activity"]["failed_logins"]

        if failed_logins >= 3:
            risk_score += 0.3        # multiple failed logins = risky
        elif failed_logins >= 1:
            risk_score += 0.1

        if file_access > 10:
            risk_score += 0.2        # excessive file access = risky

        # Clamp risk_score to [0.0, 1.0]
        risk_score = min(risk_score, 1.0)

        self.state["risk_score"] = round(risk_score, 2)

        # --- Reward Calculation ---
        reward = 0.0

        if risk_score >= 0.6:
            # High risk — blocking/quarantining is correct
            if action in ["block", "quarantine"]:
                reward = 1.0
            elif action == "monitor":
                reward = 0.3
            else:
                reward = -1.0   # allowing a high-risk event is bad
        elif risk_score >= 0.3:
            # Medium risk — monitoring is ideal
            if action == "monitor":
                reward = 1.0
            elif action in ["block", "quarantine"]:
                reward = 0.5
            else:
                reward = -0.5
        else:
            # Low risk — allowing is correct
            if action == "allow":
                reward = 1.0
            elif action == "monitor":
                reward = 0.5
            elif action in ["block", "quarantine"]:
                reward = -0.5   # overreacting to low risk

        # Episode ends after one decision
        self.done = True

        self.history.append({
            "state": self.state,
            "action": action,
            "reward": reward,
        })

        return self.state, reward, self.done


# --- Quick Test ---
if __name__ == "__main__":
    env = SecurityEnv()

    # Scenario 1: Normal office login
    state = env.reset()
    print("=== Scenario 1: Normal Office Login ===")
    print(f"State: {state}")
    state, reward, done = env.step("allow")
    print(f"Action: allow | Risk: {state['risk_score']} | Reward: {reward}\n")

    # Scenario 2: Late-night unknown location with failed logins
    state = env.reset()
    state["login_time"] = 2
    state["location"] = "unknown"
    state["activity"]["failed_logins"] = 5
    state["activity"]["file_access"] = 15
    print("=== Scenario 2: Suspicious Activity ===")
    print(f"State: {state}")
    state, reward, done = env.step("block")
    print(f"Action: block | Risk: {state['risk_score']} | Reward: {reward}\n")

    # Scenario 3: Wrong response to high risk
    state = env.reset()
    state["login_time"] = 3
    state["location"] = "unknown"
    state["activity"]["failed_logins"] = 4
    print("=== Scenario 3: Bad Decision on High Risk ===")
    print(f"State: {state}")
    state, reward, done = env.step("allow")
    print(f"Action: allow | Risk: {state['risk_score']} | Reward: {reward}")
