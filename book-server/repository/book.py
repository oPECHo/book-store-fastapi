from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    books = db.query(models.Book).all()
    return books

def create(request,db: Session):
    new_book = models.Book(title=request.title, price=request.price, stockAmount=request.stockAmount, category=request.category)
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
    db.commit()
    return 'updated'

def show(id:int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail=f'Book with the id {id} is not available')
    return book