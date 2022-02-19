# from typing import List
#
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
#
# from backend.db import crud
# from backend.db import models, schema
# from backend.db import SessionLocal, engine
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @app.post("/users/", response_model=schema.User)
# def create_user(user: schema.User, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=List[schema.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schema.Pupil)
# def create_item_for_user(
#     user_id: int, pupil: schema.Pupil, db: Session = Depends(get_db)
# ):
#     return crud.create_pupil(db=db, pupil=pupil, user_id=user_id)
#
#
# @app.get("/items/", response_model=List[schema.Pupil])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     pupils = crud.get_pupils(db, skip=skip, limit=limit)
#     return pupils
