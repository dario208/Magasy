from sqlalchemy.orm import Session
from models.models import User
from core.database import get_session
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = next(get_session())
    try:
        yield db
    finally:
        db.close()

class UserBase(BaseModel):
    email: EmailStr
    name: str  # Combine first and last names for simplicity
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

    @validator("password", pre=True)
    def validate_password(cls, value):
        if value is not None and len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

def create_user(db: Session, user_create: UserCreate):
    hashed_password = pwd_context.hash(user_create.password)
    db_user = User(email=user_create.email, hashed_password=hashed_password, name=user_create.name, role=user_create.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()