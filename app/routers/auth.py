from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.deps.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(
        email=user.email,
        username=user.username,
        password_hash=hash_password(user.password),
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="User with these data already exists"
        )

    return {"message": "user created"}


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
