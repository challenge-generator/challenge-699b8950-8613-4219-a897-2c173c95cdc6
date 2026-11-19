from fastapi import FastAPI
from app.app import create_app
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app: FastAPI = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("ENVIRONMENT", "development") == "development"
    )