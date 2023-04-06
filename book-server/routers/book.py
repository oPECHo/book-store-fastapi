from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import book

router = APIRouter(
    prefix="/book",
    tags=['Books']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBook])
async def Search(id: Optional[int] = Query(None), db : Session = Depends(get_db),categoryId: Optional[int] = Query(None)):
    return book.Search(id, db, categoryId)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Book, db : Session = Depends(get_db)):
    return book.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def destory(id:int, db: Session = Depends(get_db)):
    return book.destory(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(id:int, request: schemas.Book, db: Session = Depends(get_db)):
    return book.update(id, request, db)
