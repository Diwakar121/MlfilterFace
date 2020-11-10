#camera.py
# import the necessary packages
import cv2
import numpy as np
# defining face detector

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
# nose_cascade = cv2.CascadeClassifier("Nose18x15.xml")
# eyes_cascade = cv2.CascadeClassifier("frontalEyes35x16.xml")
# chasme = cv2.imread('glas2.png',cv2.IMREAD_UNCHANGED)
# much = cv2.imread('mustache.png',cv2.IMREAD_UNCHANGED)



class VideoCamera(object):
    def __init__(self,filter_type):
       #capturing video
       self.video = cv2.VideoCapture(0)
       self.filter = filter_type

    
    def __del__(self):
        #releasing camera
        self.video.release()
    def get_frame(self):
            ret, img = self.video.read()
            # if int(self.filter) ==0:
            ret, jpeg = cv2.imencode('.jpg', img)
                
            return jpeg.tobytes()


        
            chasme_type = 'glas'+str(self.filter)+'.png'
            much_type = 'mustache'+str(self.filter)+'.png'
            # print(self.filter)
            chasme = cv2.imread(chasme_type,cv2.IMREAD_UNCHANGED)
            much = cv2.imread(much_type,cv2.IMREAD_UNCHANGED)
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    # faces =  face_cascade.detectMultiScale(img,1.3,4) 
            faces =  face_cascade.detectMultiScale(img,1.3,4)
            eyes =  eyes_cascade.detectMultiScale(img,1.3,4)
            noses =  nose_cascade.detectMultiScale(img,1.3,4)
    
            for face in faces:
                x,y,w,h =face
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

            for (ex, ey, ew, eh) in eyes:
                mg=20
            #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
                roi_eyes = img[ey: ey + eh+mg, ex-mg: ex + ew+mg]
                glasses2 = cv2.resize(chasme.copy(),(ew+2*mg,eh+mg))
                gw, gh, gc = glasses2.shape
                for i in range(0, gw):
                    for j in range(0, gh):
                        #print(glasses[i, j]) #RGBA
                        if glasses2[i, j][3] != 0: # alpha 0
                            img[ey + i, ex+j-mg] = glasses2[i, j]

            for (nx, ny, nw, nh) in noses:
                mg=20
            
                d=(2*nh)//3
                roi_nose = img[ny+d:ny+nh+mg, nx-mg:nx+nw+mg]
                much2 = cv2.resize(much.copy(),(nw+2*mg,nh-d+mg))
                mw, mh, mc = much2.shape
                for i in range(0, mw):
                    for j in range(0, mh):
                       
                        if much2[i,j][3] != 0: # alpha 0
                            img[ny+i+d, nx+j-mg] = much2[i, j]
        
        # encode OpenCV raw frame to jpg and displaying it
           # print("hello")
            ret, jpeg = cv2.imencode('.jpg', img)

            return jpeg.tobytes()