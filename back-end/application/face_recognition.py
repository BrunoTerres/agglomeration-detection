import cv2
import io
import os  
import numpy as np
from pylab import rcParams
import urllib.request
from matplotlib import pyplot as plt
from IPython.display import display, clear_output, Image



def face_det():

#    return cv2.__version__

    os.listdir(os.curdir)
    print('pessoas.jpg' in os.listdir(os.curdir))
    
    img =cv2.imread('pessoas.jpg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)



    haarcascade_path = '/usr/local/share/opencv4/haarcascades'
    
    classifier_frontalface = 'haarcascade_frontalface_alt.xml'
    classifier_path_frontalface = os.path.join(haarcascade_path, classifier_frontalface)
    model_frontalface = cv2.CascadeClassifier(classifier_path_frontalface)

    classifier_eye = 'haarcascade_eye_tree_eyeglasses.xml'
    classifier_path_eye = os.path.join(haarcascade_path, classifier_eye)
    model_eye =cv2.CascadeClassifier(classifier_path_eye)

    eye = model_eye.detectMultiScale(img_gray)
    frontalface = model_frontalface.detectMultiScale(img_gray)

    for x, y, h, w in frontalface:
        img_det = cv2.rectangle(img_rgb, (x,y), (x+w, y+h), (255),2)

        for x, y, h, w in eye:
            img_eye = cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255), 2)

    
    print(img_det)
