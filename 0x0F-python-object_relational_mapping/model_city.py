#!/usr/bin/python3
"""
contains the class City
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Representation of a city
    - attribute id that represents a column of
    an auto-generated, unique integer, cant be null and is a primary key
    - attribute name that represents a column
    of a string of 128 characters and cant be null"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
