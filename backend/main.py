from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from .db import schema, crud, models
from .db.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"API": "BAS", "version": "0.1"}


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schema.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schema.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post(
    "/users/pupils/", response_model=schema.Pupil, status_code=status.HTTP_201_CREATED
)
def create_pupils(pupil: schema.PupilCreate, db: Session = Depends(get_db)):
    if not crud.get_user_by_id(db, int(pupil.parent_id)):
        raise HTTPException(
            status_code=404, detail=f"user {pupil.parent_id} doesn't exist"
        )
        # return schema.UserNotExist(error="User not found", message=f"user {pupil.parent_id} doesn't exist")
    return crud.create_pupil(db=db, pupil=pupil)


@app.get("/pupils/", response_model=List[schema.Pupil])
def get_pupils(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pupils = crud.get_pupils(db, skip=skip, limit=limit)
    return pupils


@app.get("/pupils/{pupil_id}", response_model=schema.Pupil)
def get_pupil_by_id(pupil_id: int, db: Session = Depends(get_db)):
    pupils = crud.get_pupil_by_id(pupil_id=pupil_id, db=db)
    return pupils


@app.get("/pupils/{pupil_id}/parent", response_model=schema.UserResponse)
def get_parent_using_pupil_id(pupil_id: int, db: Session = Depends(get_db)):
    parent = crud.get_parent_pupil_id(pupil_id=pupil_id, db=db)
    if parent:
        return parent
    else:
        raise HTTPException(
            status_code=404, detail=f"Pupil id: {pupil_id} doesn't exist"
        )
