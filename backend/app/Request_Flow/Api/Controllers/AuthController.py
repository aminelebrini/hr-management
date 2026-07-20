from sqlalchemy.orm import Session
from app.Request_Flow.Api.Services.AuthService import AuthService


class AuthController:

    def __init__(self, db: Session):
        self.auth_service = AuthService(db)

    def login(self, login_data):
        return self.auth_service.login(login_data)
