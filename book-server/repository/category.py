from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas
from fastapi import HTTPException, status, Depends, Query
from ..database import get_db



def Search(
    db: Session = Depends(get_db),
    id: Optional[int] = Query(None)
):
    if id is not None:
        category = db.query(models.Category).filter(models.Category.id == id).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Category with the ID [{id}] is not available')
        return [category]
    
    categories = db.query(models.Category).all()
    return categories


def create(request,db: Session):
    new_category = models.Category(title=request.title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def destory(id:int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Category with id {id} not found')
    category.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:schemas, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Category with id {id} not found')
    category.title = request.title
    db.commit()
    return 'updated'
