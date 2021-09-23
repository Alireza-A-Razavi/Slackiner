from typing import List
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr
from sqlalchemy.util.langhelpers import public_factory

Base = declarative_base()

class CoinOrm(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    acr = Column(String(6), unique=True)
    price = Column(Float)
    domains = Column(ARRAY(String(255)))


class CoinModel(BaseModel):
    id: int 
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    acr: constr(max_length=6)
    domain: List(constr(max_length=225))

    class Config:
        orm_mode = True


class PairOrm(Base):
    __table__ = "pairs"
    id = Column(ForeignKey())

class Pair(BaseModel):
    id: int
    first: 