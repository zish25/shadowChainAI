<<<<<<< HEAD
"""Decision module for Round 1 security simulation."""


def choose_action(risk_score):
    """Choose an action using simple threshold-based policy."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"
=======
"""Decision module for Round 1 security simulation."""


def choose_action(risk_score):
    """Choose an action using simple threshold-based policy."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"
>>>>>>> a245b326e450f824f89a15e4567ef5a8ba1a17fe
