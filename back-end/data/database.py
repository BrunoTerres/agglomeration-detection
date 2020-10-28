from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:12345678@localhost:50050/cybertech', echo=True)

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

#tabelas
from data.models.salas_model import Salas
from data.models.cameras_model import Cameras
from data.models.usuarios_model import Usuarios 
from data.models.alert_model import Alerts
from data.models.report_model import Reports
from data.models.frame_model import Frames

Base.metadata.create_all(engine)

def session_factory():
    return _SessionFactory()
