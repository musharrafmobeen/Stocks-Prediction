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


# def getPic():
#     camera = cv2.VideoCapture(0)
#     if camera is None or not (camera.isOpened()):
#         cam = Device()
#         url = 'images/known/' + rs.get_random_string(8) + '.jpg'
#         cam.saveSnapshot(url)
#         return url
#
#     else:
#         print('No Capture Device Available')
def getPic():
    name = rs.get_random_string(8) + '.jpg'

    response = requests.get("http://192.168.10.7:8080/photo.jpg")
    img1 = Image.open(BytesIO(response.content))
    img1.save('images/unknown/' + name)
    return name

def compare(img):
    folder = './images/known/'
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        img_encoded = fr.face_encodings(image)[0]
        result = fr.compare_faces([img],img_encoded,tolerance=0.5)
        if result[0]:
            print('person found')
            cv2.imshow('img',image)
            cv2.waitKey()
            return True  
            


def SignUp_With_FacialId():
    name = getPic()
    # url = './images/unknown/images.jpg'
    image = fr.load_image_file('images/unknown/' + name)

    face_locations = fr.face_locations(image)


    if(len(face_locations) == 1):
        img = fr.face_encodings(image)[0]
        if compare(img):
            print('Account Already Exists')
            os.remove('images/unknown/' + name)
          
        else:
            cv2.imwrite('images/known/' + name, image)
            print('Person Saved')  
            os.remove('images/unknown/' + name)


    elif(len(face_locations) > 1):
        print('More Than One person in Image')
        os.remove('images/unknown/' + name)

    else:
        print('NO person in image')
        os.remove('images/unknown/' + name)

def SignIn_With_FacialId():
    name = getPic()

    image = fr.load_image_file('images/unknown/' + name)

    face_locations = fr.face_locations(image)


    if(len(face_locations) == 1):
        img = fr.face_encodings(image)[0]
        if not compare(img):
            print('Sign Up First')
        else:
            print('Logged In')
            os.remove('images/unknown/' + name)

    elif(len(face_locations) > 1):
        print('More Than One person in Image')

    else:
        print('NO person in image')



