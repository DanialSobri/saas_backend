import sys
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.db import SessionLocal, engine

def create_user(db: Session, username: str, email: str, password: str):
    """
    Function to create a user in the database.
    """
    user = User(username=username, email=email)
    user.set_password(password)
    db.add(user)
    db.commit()

def main():
    # Create the database tables if they don't exist
    User.metadata.create_all(bind=engine)

    # Create a new database session
    db = SessionLocal()

    # Read user input for username, email, and password
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Create the user in the database
    create_user(db, username, email, password)

    # Close the database session
    db.close()

if __name__ == "__main__":
    main()
