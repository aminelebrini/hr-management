from app.Request_Flow.Models.User import User
from sqlalchemy.orm import Session


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data):
        user = User(
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            cin=data.cin,
            username=data.username,
            password=data.password,
            role=data.role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return {
            "message": "Employee created successfully",
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
        }

    def email_exists(self, email):
        return self.db.query(User).filter(User.email == email).first() is not None

    def cin_exists(self, cin):
        return self.db.query(User).filter(User.cin == cin).first() is not None

    def username_exists(self, username):
        return self.db.query(User).filter(User.username == username).first() is not None
