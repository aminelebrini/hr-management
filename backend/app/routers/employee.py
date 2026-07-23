from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.employee import CreateEmployeeRequest
from app.Request_Flow.Api.Controllers.EmployeeController import EmployeeController
from app.database.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/employees")
async def create_employee(data: CreateEmployeeRequest, db: Session = Depends(get_db)):
    controller = EmployeeController(db)
    return controller.create(data)
