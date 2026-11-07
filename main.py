
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Dockerized Python API")

@app.get("/")
def home():
    return {"message": "Welcome to my Dockerized Python API"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
