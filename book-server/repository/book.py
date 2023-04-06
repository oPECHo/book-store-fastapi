from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Query
from .. import schemas, models
from ..database import get_db

def Search(
    id:Optional[int] = Query(None),
    db: Session = Depends(get_db),
    categoryId: Optional[int] = Query(None)
):
    
    if not id and not categoryId:
        books_with_categories = db.query(models.Book).join(models.Category, models.Book.categoryId == models.Category.id).all()

        books = []
        for book in books_with_categories:
            book_dict = {
                'id': book.id,
                'title': book.title,
                'price': book.price,
                'stockAmount': book.stockAmount,
                'category': {
                    'id': book.category.id,
                    'title': book.category.title
                }
            }
            books.append(book_dict)

        return books
    
    if id:
        book = db.query(models.Book).filter(models.Book.id == id).join(models.Category, models.Book.categoryId == models.Category.id).first()
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with the ID [{id}] is not available')
        book_dict = {
            'id': book.id,
            'title': book.title,
            'price': book.price,
            'stockAmount': book.stockAmount,
            'category': {
                'id': book.category.id,
                'title': book.category.title
            }
        }
        return [book_dict]

    if categoryId:
        books_with_categories = db.query(models.Book).filter(models.Book.categoryId == categoryId).join(models.Category, models.Book.categoryId == models.Category.id).all()
        if not books_with_categories:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with the Type [{categoryId}] is not available')
        books = []
        for book in books_with_categories:
            book_dict = {
                'id': book.id,
                'title': book.title,
                'price': book.price,
                'stockAmount': book.stockAmount,
                'category': {
                    'id': book.category.id,
                    'title': book.category.title
                }
            }
            books.append(book_dict)
        return books
    
def create(request,db: Session):
    new_book = models.Book(title=request.title, price=request.price, stockAmount=request.stockAmount, categoryId=request.categoryId)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def destory(id:int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with id {id} not found')
    book.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:schemas, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with id {id} not found')
    book.title = request.title
    book.price = request.price
    book.stockAmount = request.stockAmount
    book.categoryId = request.categoryId
    db.commit()
    return 'updated'
