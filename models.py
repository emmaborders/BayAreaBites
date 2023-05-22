from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)
    style = Column(TEXT, nullable=False)
    address = Column(TEXT, nullable=False)
    city = Column(TEXT, nullable=False)
    price = Column(INTEGER, nullable=False)
    image_url = Column(TEXT, nullable=False)

class User(Base):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT, unique=True, nullable=False)
    password = Column(TEXT, nullable=False)
    favorties = relationship("Restaurant", secondary="favorite")


class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey('user.id'), nullable=False)
    restaurant_id = Column(INTEGER, ForeignKey('restaurant.id'), nullable=False)
    
