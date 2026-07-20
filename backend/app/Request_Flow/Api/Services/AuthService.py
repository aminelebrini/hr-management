from sqlalchemy.orm import Session
from app.Request_Flow.Api.Repository.AuthRepository import AuthRepository


class AuthService:
    def __init__(self, db: Session):
        self.auth_repository = AuthRepository(db)

    def login(self, login_data):
        return self.auth_repository.login(login_data)
