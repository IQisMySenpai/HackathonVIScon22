from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="Webinterface", html=True), name="static")

@app.get("/api")
async def root():
    return {"message": "Hello World"}