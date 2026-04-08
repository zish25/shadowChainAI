from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.api_route("/ok", methods=["GET", "POST"])
async def ok(request: Request):
    try:
        await request.json()
    except:
        pass

    return {"status": "ok"}

# 🔥 IMPORTANT: catch ALL unknown routes
@app.api_route("/{full_path:path}", methods=["GET", "POST"])
async def catch_all(full_path: str, request: Request):
    return {"status": "ok"}