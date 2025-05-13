from fastapi import FastAPI
from routes import router
import os

app = FastAPI()

# Ensure that the uploads folder is present
os.makedirs('uploads',exist_ok=True)

app.include_router(router)