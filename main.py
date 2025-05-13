from fastapi import FastAPI
from routes import router
import os
from database import Base, engine

app = FastAPI()

# Ensure that the uploads folder is present
os.makedirs('uploads',exist_ok=True)

Base.metadata.create_all(engine)

app.include_router(router)