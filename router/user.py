from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_users
router = APIRouter(
    prefix='/user',
    tags=['user']
)

# create user


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_users.create_user(db, request)


# read all users
@router.get('/user', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_users.get_all_users(db)


# read user
@router.get('/{id}]', response_model=UserDisplay)
def get_user(id: int,  db: Session = Depends(get_db)):
    return db_users.get_user(db, id)


# update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_users.update_user(db, id, request)


# delete user

@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_users.delete_user(db, id)
