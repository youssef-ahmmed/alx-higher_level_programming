#!/usr/bin/python3
""" file that contains the class definition of a State and an instance Base"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Define State class"""
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column('name', String(128), nullable=False)
