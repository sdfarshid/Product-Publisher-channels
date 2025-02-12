import logging
from fastapi import FastAPI
from app.api.v1.routers import api_router

logging.basicConfig(
    level=logging.DEBUG,  # (DEBUG, INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/app.log")
    ]
)

app = FastAPI(title="User Service", version="1.0")

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello World Farshid"}
