from fastapi import FastAPI, Request

app = FastAPI(root_path="")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/ok")
async def ok(request: Request):
    try:
        await request.json()
    except:
        pass

    return {"status": "ok"}