import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user = relationship("user.id")
    planet = relationship("planet.id")
    vehicle = relationship("vehicle.id")
    character = relationship("character.id")

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    suscription_date = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("favorite.id"))

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("favorite.id"))

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("favorite.id"))





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
