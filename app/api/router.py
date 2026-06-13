from fastapi import APIRouter 
from app.api.routers import health
from app.api.routers import users

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(users.router)




