from sqlalchemy.orm import Session
from app.Request_Flow.Models.User import User

def seed_users(db: Session):
    users = [
        User(
            full_name="AMINE LEBRINI", 
             username="aminelebrini", 
             email="aminel@hr.com",
                cin="123456789",
                phone="1234567890",
                password="password123"
             )]
    
    db.add_all(users)
    db.commit()