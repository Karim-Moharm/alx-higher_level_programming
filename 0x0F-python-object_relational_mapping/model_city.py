#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
Base = declarative_base()


class City(Base):
    """Cites class for cites table in DB
    """
    __tablename__ = 'cities'

    Column('id', Integer(), unique=True, autoincrement=True,
           nullable=False, primary_key=True)
    Column('name', String(128), nullable=False)
    Column("state_id", Integer(), ForeignKey("states.id"), nullable=False)
