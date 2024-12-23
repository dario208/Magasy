from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from api.users.users_services import (  # Assuming users_services.py is in the same directory
     UserBase, UserCreate, get_users, create_user, get_db, UserUpdate, update_user
)
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/get", response_model=List[UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieves a list of users with pagination (optional `skip` and `limit` parameters).

    Raises:
        HTTPException: If an error occurs during database access.
    """
    try:
        users = get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/create", response_model=UserBase)
async def create_user_route(user_create: UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user in the database.

    Raises:
        HTTPException: If an error occurs during database access.
    """
    try:
        user = create_user(db, user_create)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
@router.put("/update", response_model=UserBase)
async def update_user_route(user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Updates an existing user in the database.

    Raises:
        HTTPException: If an error occurs during database access.
    """
    user = db.query(UserBase).filter(UserBase.id == user_update.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = update_user(db, user_update)
    return updated_user