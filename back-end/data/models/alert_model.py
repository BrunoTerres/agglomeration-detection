from sqlalchemy import Column, String, Integer
from data.database import Base

class Alerts(Base):
    __tablename__ = 'alerts'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    alert_text = Column(String(255))


    def __init__(self, name, alert_text):
        self.name = name
        self.alert_text = alert_text

