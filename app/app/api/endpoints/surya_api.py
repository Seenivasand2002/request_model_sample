from fastapi import *
from schemas import *
import requests

router = APIRouter()

@router.post("/get_surya_root")
async def getRoot():
    url = "http://192.168.4.26:8000/user/root"
    try:
      response_from_api = requests.post(url=url)
      res = response_from_api.json()
      return {"message": res["message"]}
    except:
        raise HTTPException(status_code=500, detail="Something went worng") 

@router.post("/create_employee_by_surya_api")
async def postSuryaApiData(employee_in : EmpData):
    url = "http://192.168.4.26:8000/user/create-Customer"
    
    try:
      response_from_api = requests.post(url=url,json=employee_in.dict())
      res = response_from_api.json()
      return {"message": res["message"]}
    except:
        raise HTTPException(status_code=500, detail="Something went worng")

@router.post("/get_surya_employee/{employee_id}")
async def getSuryaEmp(employee_id: int):
    url = f"http://192.168.4.26:8000/user/view-Employee-details/{employee_id}"
    try:
      response_from_api = requests.post(url=url)
      return response_from_api.json()
    except:
        raise HTTPException(status_code=500, detail="Something went worng")
    
@router.post("/get_list_of_employee_in_surya_api")
async def getListOfEmpInSuryaApi():
    url = "http://192.168.4.26:8000/user/list-all-employee"
    try:
      responses_from_api = requests.post(url=url)
      return responses_from_api.json()
    except:
        raise HTTPException(status_code=500, detail="Something went worng")

@router.post("/get_list_of_employee_using_pagination")
async def suryaPagination(page: int = Query(1,ge=1),size: int = Query(10,ge=1)):
    url = f"http://192.168.4.26:8000/user/pagination?page={page}&size={size}"
    try:
      responses_from_api = requests.post(url=url)
      return responses_from_api.json()
    except:
        raise HTTPException(status_code=500, detail="Something went worng")