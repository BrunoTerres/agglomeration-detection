import sys 

sys.path.append('/home')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
#from data.dao.frames_dao import Frame_dao
from application.face_recognition import face_det



class FrameAPI(RequestHandler):

    def get(self):

        self.write({'face_det' : face_det()})


def make_app():

    urls = [
        ('/api/one/', FrameAPI)
    ]

    return Application(urls)

def start_service():

    app = make_app()
    app.listen(8001)
    IOLoop.instance().start()

if __name__ == '__main__':
    start_service()