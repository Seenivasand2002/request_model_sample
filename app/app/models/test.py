from db import Base
from sqlalchemy import *

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer,autoincrement=True,primary_key=True)
