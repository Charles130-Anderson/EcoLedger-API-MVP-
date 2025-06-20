from fastapi import FastAPI
from .routes import credits

app = FastAPI(
    title="EcoLedger MVP API",
    version="0.1",
    description="API for managing carbon credit records"
)

app.include_router(credits.router)
