"""Evaluation module for Round 1 security simulation."""


def expected_action(risk_score):
    """Return expected best action for a given risk score."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"


def evaluate_decision(risk_score, action):
    if action == expected_action(risk_score):
        return 0.9   # correct decision
    else:
        return 0.1   # wrong decision