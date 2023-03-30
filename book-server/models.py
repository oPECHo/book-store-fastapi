from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title =Column(String)
    price = Column(Integer)
    stockAmount = Column(Integer)
    category = Column(Integer, ForeignKey('categorys.id'))

    type = relationship("Category", back_populates="book")

class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    book = relationship("Book", back_populates="type")