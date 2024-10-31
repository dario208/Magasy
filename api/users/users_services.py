from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from sqlalchemy.orm import Session
from models.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserBase(BaseModel):
    email: EmailStr
    name: str  # Combine first and last names for simplicity
    role: str


class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_password(cls, value):
        if not value:
            raise ValueError("Password cannot be empty")
        return value


class UserUpdate(UserBase):
    password: Optional[str] = None

    @validator("password", pre=True)
    def validate_password(cls, value):
        if value is not None and len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    """Retrieves a list of users with pagination."""
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user_create: UserCreate) -> User:
    """Creates a new user with a hashed password."""
    db_user = User(
        email=user_create.email,
        name=user_create.name,
        hashed_password=user_create.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user