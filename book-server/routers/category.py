from typing import List, Optional
from fastapi import APIRouter, Depends, status, Response, Query
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import category

router = APIRouter(
    prefix="/category",
    tags=['Categorys']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowCategory])
async def Search(db : Session = Depends(get_db), id: Optional[int] = Query(None)):
    return category.Search(db, id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Category, db : Session = Depends(get_db)):
    return category.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def destory(id:int, db: Session = Depends(get_db)):
    return category.destory(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(id:int, request: schemas.Category, db: Session = Depends(get_db)):
    return category.update(id, request, db)
