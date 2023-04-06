from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title =Column(String)
    price = Column(Float)
    stockAmount = Column(Integer)
    categoryId = Column(Integer, ForeignKey("categorys.id"))

    category = relationship("Category", back_populates="books")


class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    books = relationship("Book", back_populates="category")