from fastapi import FastAPI
from pydantic import BaseModel

from ml_model import predict_risk
from decision_module import choose_action

app = FastAPI()

class InputData(BaseModel):
    login_time: int
    location: str
    file_access: int
    failed_logins: int

@app.post("/ok")
def process(data: InputData):
    features = [
        data.login_time,
        1 if data.location == "unknown" else 0,
        data.file_access,
        data.failed_logins,
    ]

    risk = predict_risk(features)
    action = choose_action(risk)

    return {
        "risk_score": risk,
        "action": action
    }