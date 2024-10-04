from fastapi import *
from schemas import EmployeeIn,EmpData
from models import Employee
from typing import Annotated, List
from sqlalchemy.orm import Session
from api.deps import get_db
from fastapi_pagination import Page,add_pagination,paginate
import math

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

@router.post("/{employee_id}/details")
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

@router.post("/get_list_of_employee",response_model=list[EmployeeIn])
async def getListOfemp(
    db: Annotated[Session, Depends(get_db)]
):
    db_employee = db.query(Employee).all()
    return db_employee

@router.post("/get_list_of_employee_using_pagenation",response_model=Page[EmployeeIn])
async def getListOfemp(
    db: Annotated[Session, Depends(get_db)]
):
    """
    using fastapi-pagination method
    """
    db_employee = db.query(Employee).all()
    return paginate(db_employee)

add_pagination(router)

@router.post("/get_list_of_employee_pagination")
async def getListOfempWithOutModel(
    db: Annotated[Session, Depends(get_db)],
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1)
):
    start = (page - 1) * size
    total_count = db.query(Employee).count()
    no_of_pages = 1 if int(total_count/size) <= 0 else math.ceil(total_count/size)

    db_employee = db.query(Employee).offset(start).limit(size).all()
    return {
        "employees": db_employee,
        "total": total_count,
        "page": page,
        "size": size,
        "no of page": no_of_pages
    }



   

    
    

 



