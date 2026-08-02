from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import String, Boolean, DateTime, func
from datetime import datetime

class User(Base):
    __tablename__ = "users" #Defining the table name for the User model

    id: Mapped[int] = mapped_column(primary_key=True, index=True) #Defining the id column as primary key and indexed
    full_name: Mapped[str] = mapped_column(String) #Defining the full_name column
    email: Mapped[str] = mapped_column(String, unique=True, index=True) #Defining the email column as unique and indexed
    hashed_password: Mapped[str] = mapped_column(String) #Defining the hashed_password column
    is_active: Mapped[bool] = mapped_column(Boolean, default=True) #Defining the is_active column with a default value of True
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) #Defining the created_at column with a default value of the current timestamp

