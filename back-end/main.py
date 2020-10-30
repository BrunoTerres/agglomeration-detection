from data.database import session_factory
from data.dao.alert_dao import Alert_dao
from data.dao.camera_dao import Camera_dao
from data.dao.frame_dao import Frame_dao
from data.dao.report_dao import Report_dao
from data.dao.sala_dao import Sala_dao
from data.dao.usuario_dao import User_dao



def main():

    frame = Frame_dao.create_frame('baby')



if __name__ ==  '__main__':
    main()