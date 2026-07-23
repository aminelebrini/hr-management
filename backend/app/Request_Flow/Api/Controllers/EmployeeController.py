from sqlalchemy.orm import Session
from app.Request_Flow.Api.Services.EmployeeService import EmployeeService


class EmployeeController:
    def __init__(self, db: Session):
        self.employee_service = EmployeeService(db)

    def create(self, data):
        return self.employee_service.create(data)
