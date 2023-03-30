from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    price: int
    stockAmount: int
    category: int

class Book(BlogBase):
    class Config():
        orm_mode = True

class CategoryBase(BaseModel):
    title: str

class Category(CategoryBase):
    class Config():
        orm_mode = True

class ShowCategory(BaseModel):
    title: str
    book : List[Book] = []
    class Config():
        orm_mode = True

class ShowBook(BaseModel):
    title: str
    price: int
    stockAmount: int

    class Config():
        orm_mode = True