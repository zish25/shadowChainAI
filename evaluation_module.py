"""Evaluation module for Round 1 security simulation."""


def expected_action(risk_score):
    """Return expected best action for a given risk score."""
    if risk_score >= 0.6:
        return "block"
    if risk_score >= 0.3:
        return "monitor"
    return "allow"


def evaluate_decision(risk_score, action):
    risk = max(0.01, min(risk_score, 0.99))
    expected = expected_action(risk)

    # Use three graders to produce a richer, dynamic score profile.
    if action == "allow":
        confidence = 1 - (risk * 0.75)
    elif action == "block":
        confidence = (risk * 0.85) + 0.05
    else:
        confidence = 0.45 + (risk * 0.20)

    alignment = 0.98 if action == expected else 0.42
    risk_consistency = 1 - abs(risk - 0.5)

    task_graders = {
        "confidence_grader": confidence,
        "alignment_grader": alignment,
        "consistency_grader": risk_consistency,
    }

    weighted_score = (
        task_graders["confidence_grader"] * 0.50
        + task_graders["alignment_grader"] * 0.30
        + task_graders["consistency_grader"] * 0.20
    )

    # Strictly inside (0, 1) while avoiding hard endpoints.
    score = min(max(weighted_score, 0.001), 0.999)

    return score