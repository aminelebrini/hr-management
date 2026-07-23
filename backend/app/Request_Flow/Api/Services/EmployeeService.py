from sqlalchemy.orm import Session
from app.Request_Flow.Api.Repository.EmployeeRepository import EmployeeRepository


class EmployeeService:
    def __init__(self, db: Session):
        self.employee_repository = EmployeeRepository(db)

    def create(self, data):
        if self.employee_repository.email_exists(data.email):
            return {"error": "Email already exists"}
        if self.employee_repository.cin_exists(data.cin):
            return {"error": "CIN already exists"}
        if self.employee_repository.username_exists(data.username):
            return {"error": "Username already exists"}
        return self.employee_repository.create(data)
