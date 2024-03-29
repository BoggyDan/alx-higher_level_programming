#!/usr/bin/python3
"""
Creates a model
"""


from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Class with an id and attributes
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
