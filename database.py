from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found, check .env file")

# Create the engine or connection between SQLAlchemy and PostGreSQL
engine = create_engine(DATABASE_URL)

#Create Session
SessionLocal = sessionmaker(autoflush=False, bind=engine)

#Create ORM Base
Base = declarative_base()