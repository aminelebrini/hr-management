from pydantic import BaseModel
from typing import Optional


class CreateEmployeeRequest(BaseModel):
    full_name: str
    email: str
    phone: Optional[str] = None
    cin: str
    username: str
    password: str
    role: str
    department: Optional[str] = None
    position: Optional[str] = None
    contract_type: Optional[str] = None
    start_date: Optional[str] = None
