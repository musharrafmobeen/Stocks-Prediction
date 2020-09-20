import face_recognition as fr
import RandomString as rs
import numpy as np
from cv2 import cv2
from io import BytesIO
import requests
import os
import shutil
from VideoCapture import Device
from PIL import Image
 


def compare(img):
    folder = './images/known/'
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        img_encoded = fr.face_encodings(image)[0]
        result = fr.compare_faces([img],img_encoded,tolerance=0.5)
        if result[0]:
            return filename

              
            


def SignUp_With_FacialId(PicName):
    text = '' 
    name = PicName
    image = fr.load_image_file('images/unknown/' + name)

    face_locations = fr.face_locations(image)


    if(len(face_locations) == 1):
        img = fr.face_encodings(image)[0]
        image2 = compare(img)
        if image2 != None:
            text = 'Account Already Exists'
            os.remove('images/unknown/' + name)
            return text
          
        else:
            cv2.imwrite('images/known/' + name, image)
            text = 'Person Saved' 
            os.remove('images/unknown/' + name)
            return text


    elif(len(face_locations) > 1):
        text = 'More Than One person in Image'
        os.remove('images/unknown/' + name)
        return text

    else:
        text = 'NO person in image'
        os.remove('images/unknown/' + name)
        return text

def SignIn_With_FacialId(PicName):
    text = ''
    name = PicName

    image = fr.load_image_file('images/unknown/' + name)

    face_locations = fr.face_locations(image)


    if(len(face_locations) == 1):
        img = fr.face_encodings(image)[0]
        image2 = compare(img) 
        if image2 == None:
            text = 'Sign Up First'
            os.remove('images/unknown/' + name)
            return text

        else:
            text = image2
            os.remove('images/unknown/' + name)
            return text

    elif(len(face_locations) > 1):
        text ='More Than One person in Image'
        return text

    else:
        text = 'NO person in image'
        return text



