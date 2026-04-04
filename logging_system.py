<<<<<<< HEAD
"""Basic logging module for Round 1 security simulation."""


class BasicLogger:
    """In-memory logger for scenario, action, and rewards."""

    def __init__(self):
        self.records = []

    def log_episode(self, state, risk_score, action, reward, evaluation_reward):
        self.records.append(
            {
                "state": state,
                "risk_score": risk_score,
                "action": action,
                "reward": reward,
                "evaluation_reward": evaluation_reward,
            }
        )
=======
"""Basic logging module for Round 1 security simulation."""


class BasicLogger:
    """In-memory logger for scenario, action, and rewards."""

    def __init__(self):
        self.records = []

    def log_episode(self, state, risk_score, action, reward, evaluation_reward):
        self.records.append(
            {
                "state": state,
                "risk_score": risk_score,
                "action": action,
                "reward": reward,
                "evaluation_reward": evaluation_reward,
            }
        )
>>>>>>> a245b326e450f824f89a15e4567ef5a8ba1a17fe
