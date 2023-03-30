from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import category

router = APIRouter(
    prefix="/category",
    tags=['Categorys']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowCategory])
def all(db : Session = Depends(get_db)):
    return category.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Category, db : Session = Depends(get_db)):
    return category.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id:int, db: Session = Depends(get_db)):
    return category.destory(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Category, db: Session = Depends(get_db)):
    return category.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowCategory)
def show(id:int, response: Response, db: Session = Depends(get_db)):
    return category.show(id, db)