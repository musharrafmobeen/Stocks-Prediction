from cv2 import cv2
import RandomString as rs

def getPic():
    camera = cv2.VideoCapture(0)
    name = rs.get_random_string(8) + '.jpg'
    if camera:
        while True:
            ret,image = camera.read()
            cv2.imshow('image',image)
            if cv2.waitKey(1)& 0xFF == ord('s'):
                cv2.imwrite('images/unknown/'+name,image)
                break
        cv2.destroyAllWindows()
        camera.release()
        return name 

    else:
        return "No Capture Device Available"         