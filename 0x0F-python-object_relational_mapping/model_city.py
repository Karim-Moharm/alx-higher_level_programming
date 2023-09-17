#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
# from model_state import Base
Base = declarative_base()


class City(Base):
    """Cites class for cites table in DB
    """
    __tablename__ = 'cities'

    id = Column(Integer(), unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
