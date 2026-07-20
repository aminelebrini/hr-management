from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    position_id = Column(Integer)
    contract_type = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    created_at = Column(String)
    updated_at = Column(String)