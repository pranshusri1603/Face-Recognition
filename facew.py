import cv2
import numpy as np
import face_recognition
from PIL import Image
import os

def cap_img(a):    
    cam=cv2.VideoCapture(0)
    cv2.namedWindow("Webcam Image capture")
    img_counter=0
    while True:
       ret,frame=cam.read()
       if not ret:
           print("failed to grab frame")
           break
       cv2.imshow("test",frame)
       k=cv2.waitKey(1)
       if k%256==27:
           print("Escape Pressed Clsing the Window")
           break
       elif k%256==32:
           img_name=a+"_{}.jpg".format(img_counter)
           cv2.imwrite(img_name,frame)
           print("screenshot taken")
           img_counter+=1
    
    cam.release()
    cv2.destroyAllWindows()
a=input("Enter Your Name To Be Saves On Picture")    
cap_img(a)
################################################################################

'''
def compare_cap_img():
    path='C:\\Users\\dell\\AppData\Local\\Programs\\Python\\Python310'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for i in mylist:
        curImg=cv2.imread(f'{path}/i')
        images.append(curImg)
        classNames.append(os.path.splitext(i)[0])
    #print(classNames)

    def findEncodings(images):
        encodeList=[]
        for img in images:
            #img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            encode=face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    encodeListKnown=findEncodings(images)
    print(len(encodeListKnown))
    print("Encoding Complete")


    cap=cv2.VideoCapture(0)
    while True:
        success,imgS=cap.read()
        #imgS=cv2.resize(img,(0,0),None,0.25,0.25)
        #imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
           
        facesCurframe=face_recognition.face_locations(imS)
        encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
            #faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            #matchIndex=np.argmin(faceDis)
            #if matches[matchIndex]:
                #name=classNames[matchIndex].upper()
                #print(name)
            print(matches)
            if matches[0]:
                print('welcome')
            else:
                print('Unautorized Access')
        cv2.inshow('WebCam',img)
        cv2.waitKey(1)
compare_cap_img()
'''

