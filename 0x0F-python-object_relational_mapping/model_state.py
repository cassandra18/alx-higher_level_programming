#!/usr/bin/python3

"""This module contains a class definition of a state.
It contains also an instance Base = declarative_base().
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class inherits from the Base class.
    It will represent the structure of the States table in the db.
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True
        )
    name = Column(String(128), nullable=False)
