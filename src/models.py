import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_characters = Column(Integer, ForeignKey('characters.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))

class  Users(Base):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(250), unique=True)
    password = Column(String(250))
    # Relations
    favorite_characters = relationship('characters', secondary=favorites, back_populates='users')
    favorite_planets = relationship('planets', secondary=favorites, back_populates='users')

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    # Relations
    user_favorite = relationship('users', secondary=favorites, back_populates='characaters')

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_favorite = relationship('users', secondary=favorites, back_populates='planets')
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
