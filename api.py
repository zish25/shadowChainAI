from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/ok")
async def ok(request: Request):
    data = await request.json()  # ✅ IMPORTANT

    return {
        "status": "ok",
        "received": data
    }