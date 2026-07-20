from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest
from app.Request_Flow.Api.Controllers.AuthController import AuthController
from app.database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    controller = AuthController(db)
    return controller.login(login_data)
