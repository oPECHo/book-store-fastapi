from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    price: float
    stockAmount: int
    categoryId: int

class Book(BlogBase):
    class Config():
        orm_mode = True

class CategoryBase(BaseModel):
    title: str

class Category(CategoryBase):
    class Config():
        orm_mode = True

class ShowCategory(BaseModel):
    id : int
    title : str
    class Config():
        orm_mode = True

class ShowBook(BaseModel):
    id: int
    title: str
    price: float
    stockAmount: int
    categoryId: int

    class Config():
        orm_mode = True