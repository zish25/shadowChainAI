# ShadowChainAI

ShadowChainAI is a lightweight cybersecurity decision simulation project.
It models login events, computes a risk score from contextual and behavioral signals, selects a response action, and evaluates whether the response is appropriate.

## What This Project Does

- Simulates security events (login time, location, activity).
- Computes risk using modular risk components.
- Chooses defensive actions using threshold-based policy.
- Scores outcomes with reward and evaluation modules.
- Logs each episode for analysis.

## Project Structure

- `environment.py`: Core `SecurityEnv` environment with state reset, risk/reward logic, and `step(action)` flow.
- `context_intelligence.py`: Extracts contextual risk features (time and location).
- `behavior_analysis.py`: Extracts behavioral risk features (failed logins and file access).
- `risk_engine.py`: Combines context + behavior features into a final risk score.
- `decision_module.py`: Maps risk score to action (`allow`, `monitor`, `block`).
- `evaluation_module.py`: Compares chosen action against expected action.
- `logging_system.py`: In-memory episode logger.
- `inference.py`: End-to-end multi-scenario simulation runner.
- `test_env.py`: Quick scenario-based smoke tests for `SecurityEnv`.

## Action Space

Supported actions in the environment:

- `allow`
- `monitor`
- `block`
- `quarantine`

## Risk Heuristics

The environment currently uses simple, interpretable rules:

- Time risk:
  - Late night (`<6` or `>22`) adds high risk.
  - Outside office hours (`<9` or `>17`) adds moderate risk.
- Location risk:
  - Unknown locations add risk.
- Behavior risk:
  - Multiple failed logins add risk.
  - Excessive file access adds risk.

Final score is capped to `1.0`.

## Requirements

- Python 3.9+
- No third-party dependencies required for current codebase

## Run the Project

From the project root:

```bash
python inference.py
```

Run environment smoke scenarios:

```bash
python test_env.py
```

You can also run direct environment tests:

```bash
python environment.py
```

## Example Pipeline

1. Initialize environment state with `env.reset()`.
2. Inject scenario conditions (time, location, activity).
3. Extract context and behavior features.
4. Calculate unified risk score.
5. Choose action from decision module.
6. Execute action in environment with `env.step(action)`.
7. Log and evaluate results.

## Next Improvements (Optional)

- Add unit tests with `pytest`.
- Add persistence (save logs to JSON/CSV).
- Replace rule-based policy with a trainable agent.
- Add CLI flags to run custom scenarios.
- Add visualization for risk trend and action distribution.

## License

Add a license file if you plan to share this publicly.
