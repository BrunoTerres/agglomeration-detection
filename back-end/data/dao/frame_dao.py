from 
from data.database import session_factory
from data.models.frame_model import Frames
import base64
import sys

path = '/home/bruno/Imagens/'


session = session_factory()

def get_image():
    with open(path + 'gato.jpg', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        encoded_string.decode('utf-8')
        
        return encoded_string

image = get_image()


class Frame_dao():


    def create_frame(name):
    
        frame_create = Frames(name=name, frame=image)


        session.add(frame_create)
        session.commit()

        session.close()

        return frame_create


    def get_frame(id):

        frame_get = session.query(Frames).filter(Frames.id == id).first()
        session.close()

        return frame_get