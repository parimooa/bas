from sqlalchemy.orm import Session

from . import models, schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email,
        hashed_password=fake_hashed_password,
        first_name=user.first_name,
        surname=user.surname,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_pupil_by_id(pupil_id: int, db: Session):
    student = db.query(models.Student).filter(models.Student.id == pupil_id).first()
    return student


def get_parent_pupil_id(pupil_id: int, db: Session):
    student = db.query(models.Student).filter(models.Student.id == pupil_id).first()
    if student:
        return student.parent
    else:
        return


def get_pupils(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_pupil(db: Session, pupil: schema.PupilCreate):
    pupils = models.Student(**pupil.dict())
    db.add(pupils)
    db.commit()
    db.refresh(pupils)
    return pupils
