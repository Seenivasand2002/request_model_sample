from fastapi import APIRouter
from api.endpoints import employee
from api.endpoints import surya_api

api_router = APIRouter()

api_router.include_router(employee.router, tags=["Home"])
api_router.include_router(surya_api.router, tags=["Surya API"])
