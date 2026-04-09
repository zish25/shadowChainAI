from sklearn.linear_model import LogisticRegression
import numpy as np

# Simple training data (demo purpose)
X = np.array([
    [10, 0, 3, 0],
    [2, 1, 12, 4],
    [23, 1, 8, 3],
    [14, 0, 11, 0],
    [20, 0, 5, 1],
])

y = np.array([0, 1, 1, 1, 0])  # 0=safe, 1=risky

model = LogisticRegression()
model.fit(X, y)

def predict_risk(features):
    prob = model.predict_proba([features])[0][1]
    return min(max(prob, 0.01), 0.99)