from sqlalchemy.orm import Session
from models.models import User
from core.database import get_session
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Optional
from enum import Enum

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class RoleEnum(str, Enum):
    admin = "admin"
    client = "client"
    user = "user"

def get_db():
    db = next(get_session())
    try:
        yield db
    finally:
        db.close()

class UserBase(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    role: RoleEnum

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[RoleEnum] = None
    password: Optional[str] = None

   

def create_user(db: Session, user_create: UserCreate):
    # hashed_password = pwd_context.hash(user_create.password)
    db_user = User(
        email=user_create.email,
        first_name=user_create.first_name,
        last_name=user_create.last_name,
        role=user_create.role,  # Utilisez l'énumération pour le champ role
        password=user_create.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()



def update_user(db: Session, user_id: int, user_update: UserUpdate):
    # db_user = db.query(User).filter(User.id == user_id).first()
    # if db_user:
    #     db_user.first_name = user_update.first_name
    #     db_user.last_name = user_update.last_name
    #     db_user.role = user_update.role.value  # Convertir l'énumération en chaîne de caractères
    #     db.commit()
    #     db.refresh(db_user)
    # return db_user
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    if user_update.email:
        db_user.email = user_update.email

    # Update password if provided
    if user_update.password:
        db_user.password = pwd_context.hash(user_update.password)
    
    db.commit()
    db.refresh(db_user)
    
    return {"id": user_id, "email": db_user.email}