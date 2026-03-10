from fastapi import FastAPI

app = FastAPI(title="GigGuardian AI")

@app.get("/")
def home():
    return {
        "message": "GigGuardian AI Backend Running",
        "status": "Active"
    }