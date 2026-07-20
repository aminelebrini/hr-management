from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    created_at = Column(String)
    updated_at = Column(String)