from tornado.web import Application, RequestHandler
from tornado import escape
from tornado.ioloop import IOLoop

import threading

class AbilityOneAPI(RequestHandler):
    def get(self):
        self.write({'Mensagem' : 'Esse e outro teste'})


def make_app():
    urls = [('/api/one', AbilityOneAPI)]
    return Application(urls)


def start_service():
    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()

if __name__ == "__main__":
    start_service()