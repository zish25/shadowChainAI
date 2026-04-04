"""Decision module for Round 1 security simulation."""


def choose_action(risk_score):
    """Choose an action using simple threshold-based policy."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"
