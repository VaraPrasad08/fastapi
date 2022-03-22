from sqlalchemy import Column, Integer
from .sql import Base
class info(Base):
    __tablename__="info"

    Roll_number: Column(Integer,primary_key=True,nullable=False)
    Name:Column(str,nullable=False)
    Email_addess:Column (str,nullable=False)
    Mobile_number: Column(Integer,nullable=False)
    Address: Column(str,nullable=False)
    State:Column (str,nullable=False)
    Country:Column (str,nullable=False)
    Zip:Column (int,nullable=False)

