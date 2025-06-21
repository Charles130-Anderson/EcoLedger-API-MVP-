from fastapi import FastAPI
from app.routes import credits
from app.database import engine, Base

# ✅ Register models before calling create_all()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EcoLedger MVP API",
    version="0.1",
    description="API for managing carbon credit records"
)

app.include_router(credits.router)

@app.get("/")
def root():
    return {"message": "Ecoledger is live!"}
