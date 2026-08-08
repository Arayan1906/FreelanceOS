from fastapi import FastAPI
from api.auth import router as auth_router

app = FastAPI(title="FreelanceOS API", version="1.0.0")
app.include_router(auth_router,prefix="/auth", tags=["auth"])
@app.get("/health")
def health_check():
    return {"status": "ok"}