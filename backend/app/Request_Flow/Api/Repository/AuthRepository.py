from app.Request_Flow.Models.User import User
from sqlalchemy.orm import Session


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def login(self, login_data):
        user = self.db.query(User).filter(User.email == login_data.email).first()
        if user and user.password == login_data.password:
            return {
                "message": "Login successful",
                "role": user.role,
                "full_name": user.full_name,
                "email": user.email,
            }
        else:
            return {"message": "Invalid email or password"}
