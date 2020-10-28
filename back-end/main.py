from data.database import session_factory
from data.dao.alert_dao import Alert_dao
from data.dao.cameras_dao import Camera_dao
from data.dao.frame_dao import Frame_dao
from data.dao.report_dao import Report_dao
from data.dao.salas_dao import Sala_dao
from data.dao.usuarios_dao import User_dao



def main():
    vermelho = "Aglomeracao s/ mascara"
    laranja = "Aglomeracao"


    frame = Frame_dao.create_frame('Sem mascara')


if __name__ ==  '__main__':
    main()