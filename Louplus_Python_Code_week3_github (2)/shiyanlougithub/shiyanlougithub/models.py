from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Repository(Base):
    __tablesname__='responsitories'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    update_time=Column(DateTime)
    commits=Column(Integer)
    branches=Column(Integer)
    releases=Column(Integer)
