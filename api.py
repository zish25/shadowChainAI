from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.api_route("/ok", methods=["GET", "POST"])
async def ok(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    return {
        "status": "ok"
    }