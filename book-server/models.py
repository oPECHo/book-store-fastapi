from sqlalchemy import Column, Integer, String, Float
from .database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title =Column(String)
    price = Column(Float)
    stockAmount = Column(Integer)
    categoryId = Column(Integer)


class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
