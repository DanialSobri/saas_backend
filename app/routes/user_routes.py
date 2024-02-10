from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User,UserSchema
from app.utils.db import get_db
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users/", response_model=UserSchema)
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = UserService.create_user(db=db, username=username, email=email, password=password)
    return user

@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, username: str, email: str, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = UserService.update_user(db=db, user=user, username=username, email=email)
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    UserService.delete_user(db=db, user=user)
    return {"message": "User deleted successfully"}
