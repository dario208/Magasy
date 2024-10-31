from fastapi import APIRouter
from api.users.users_routes import router as user_router

routers = APIRouter()

# Supprimez l'argument `description`
routers.include_router(user_router, prefix="/users", tags=["users"])