from app.Request_Flow.Models.User import User
from sqlalchemy.orm import Session


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def login(self, login_data):
        user = self.db.query(User).filter(User.email == login_data.email).first()
        if user and user.password == login_data.password:
            return {
                "id": user.id,
                "full_name": user.full_name,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "cin": user.cin,
                "phone": user.phone,
            }
        else:
            return {"message": "Invalid email or password"}
