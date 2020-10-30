import sys 

sys.path.append('/home/bruno/cyberTech/grupo3-rep/back-end/')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
from data.dao.camera_dao import Camera_dao

class CameraAPI(RequestHandler):

    def get(self, id):

        camera = Camera_dao.get_camera(id)

        self.write({'camera' : camera.to_json()})


def make_app():

    urls = [
        ('/api/one/([0-9]*)', CameraAPI)
    ]

    return Application(urls)

def start_service():

    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()

if __name__ == '__main__':
    start_service()