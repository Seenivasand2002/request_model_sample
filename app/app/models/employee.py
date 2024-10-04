from db import Base
from sqlalchemy import *

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    address = Column(String(200),nullable=False)