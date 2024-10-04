from fastapi import *
from schemas import EmployeeIn,EmpData
from models import Employee
from typing import Annotated, List
from sqlalchemy.orm import Session
from api.deps import get_db
import requests


router = APIRouter()

@router.post("/create_employee")
async def employee_create(
    db: Annotated[Session, Depends(get_db)],
    data_in: Annotated[EmployeeIn, Body(...)]
):
    created_data = Employee(**data_in.dict())
    db.add(created_data)
    db.commit()
    return {"message": "Successfully created", "employee_id": created_data.id}

@router.get("/{employee_id}/details")
async def getEmp(
    db: Annotated[Session,Depends(get_db)],
    employee_id: int
):
    emp_data = db.query(Employee).filter(Employee.id == employee_id).one_or_none()
    if not emp_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return emp_data

@router.get("/get_surya_root")
async def getRoot():
    url = "http://192.168.4.26:8000/user/root"
    response_from_api = requests.get(url=url)
    res = response_from_api.json()
    return {"message": res["message"]} 

@router.post("/create_employee_by_surya_api")
async def postSuryaApiData(employee_in : EmpData):
    url = "http://192.168.4.26:8000/user/create-Customer"
    response_from_api = requests.post(url=url,json=employee_in.dict())
    return dict(message = response_from_api.json())

@router.get("/get_surya_employee")
async def getSuryaEmp(employee_id: int):
    url = f"http://192.168.4.26:8000/user/view-customer-details/{employee_id}"
    response_from_api = requests.get(url=url)
    return response_from_api.json()

 
