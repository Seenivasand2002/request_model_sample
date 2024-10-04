from pydantic import *


class EmployeeIn(BaseModel):
    name: str = Field(min_length=3,max_length=100)
    age: int = Field(ge=1,le=100)
    address: str = Field(min_length=5,max_length=200)

class EmpData(BaseModel):
    name: str
    phone: str
    address: str