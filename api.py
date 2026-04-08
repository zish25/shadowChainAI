from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/ok")
def ok():
    return {
        "status": "success",
        "message": "OpenEnv endpoint working"
    }