from sqlalchemy.orm import Session
from app.models.user import User

class UserService:
    @staticmethod
    def create_user(db: Session, username: str, email: str, password: str) -> User:
        # Create a new user object
        new_user = User(username=username, email=email)
        # Set the password for the user
        new_user.set_password(password)
        
        # Add the user to the database session
        db.add(new_user)
        db.commit()
        
        return new_user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def update_user(db: Session, user: User, **kwargs) -> User:
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        db.commit()
        return user

    @staticmethod
    def delete_user(db: Session, user: User) -> None:
        db.delete(user)
        db.commit()
