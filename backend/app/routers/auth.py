from fastapi import APIRouter
from app.schemas.auth import LoginRequest
router = APIRouter()

@router.post("/login")
async def login(login_data: LoginRequest):
    return {
        "email": login_data.email,
        "password": login_data.password
    }
    