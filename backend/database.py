from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv() #Load environment variables from a .env file
engine = create_engine(os.getenv("DATABASE_URL"))#Creating an engine to connect to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#Creating a session factory to interact with db
Base = declarative_base() #Creating a base class for our models

def get_db():
    db = SessionLocal() #Creating a new database session
    try:
        yield db #Yielding the session to be used in the route
    finally:
        db.close() #Closing the session after use