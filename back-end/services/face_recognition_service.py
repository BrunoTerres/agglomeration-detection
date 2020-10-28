import sys 

sys.path.append('/home')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
from application.face_recognition import face_det

class faceRecognitionAPI(RequestHandler):

    def get(self):

        self.write({'version' : face_det()})


def make_app():

    urls = [
        ('/api/face_recognition', faceRecognitionAPI)
    ]

    return Application(urls)

def start_service():

    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()

if __name__ == '__main__':
    start_service()