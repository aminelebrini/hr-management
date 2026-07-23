from app.Request_Flow.Api.Services.AdminDataService import AdminDataService
from sqlalchemy.orm import Session
class AdminDataController:
    def __init__(self, db: Session):
        self.AdminDataService = AdminDataService(db)
    
    def get_admin_data(self):
        user = self.AdminDataService.get_admin_data()

        

        