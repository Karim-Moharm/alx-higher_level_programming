#!/usr/bin/python3
"""contains the class definition of a State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class State(Base):
    """state class for state table in DB
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, unique=True, 
            autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

