from fastapi import APIRouter
from api.endpoints import employee

api_router = APIRouter()

api_router.include_router(employee.router, tags=["Home"])
