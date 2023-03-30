from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import book

router = APIRouter(
    prefix="/book",
    tags=['Books']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBook])
def all(db : Session = Depends(get_db)):
    return book.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Book, db : Session = Depends(get_db)):
    return book.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id:int, db: Session = Depends(get_db)):
    return book.destory(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Book, db: Session = Depends(get_db)):
    return book.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBook)
def show(id:int, response: Response, db: Session = Depends(get_db)):
    return book.show(id, db)