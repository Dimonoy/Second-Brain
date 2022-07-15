from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User)\
             .filter(models.User.id == user_id)\
             .first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User)\
             .filter(models.User.email == email)\
             .first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User)\
             .offset(skip)\
             .limit(limit)\
             .all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_pages(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Page)\
             .filter(models.Page.owner_id == owner_id)\
             .offset(skip)\
             .limit(limit)\
             .all()

def create_page(db: Session, page: schemas.PageCreate, owner_id: int):
    db_page = models.Page(**page.dict(), owner_id=owner_id)
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page
