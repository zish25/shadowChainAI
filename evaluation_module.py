"""Evaluation module for Round 1 security simulation."""


def expected_action(risk_score):
    """Return expected best action for a given risk score."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"


def evaluate_decision(risk_score, action):
    """Grade decision correctness with a simple reward signal."""
    return 1.0 if action == expected_action(risk_score) else -1.0
