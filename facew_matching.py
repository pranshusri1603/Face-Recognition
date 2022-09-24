import cv2
import numpy as np
import face_recognition
from PIL import Image
import os
path='C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python310\\face id'
images=[]
classNames=[]
mylist=os.listdir(path)
print(mylist)
for cl in mylist:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) 
print(classNames)

def findEncodings(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        #faceLoc = face_recognition.face_locations(img_saved)
        #cv2.rectangle(img_saved,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
        encodelist.append(encode) 
    return encodelist
encodeListKnown=findEncodings(images)
#findEncodings(images)
print(len(encodeListKnown))
print("Encoding Complete")

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)           
    facesCurFrame=face_recognition.face_locations(imgS)
    encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame) 
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex=np.argmin(faceDis)
        print(matchIndex)
        if(matchIndex>=0):
            print("You are Identified as a Valid User")          
        #cv2.imshow('WebCam',img)
        #cv2.waitKey(1)
        break;
    break;        
cap.release()
cv2.destroyAllWindows()
print("Thank For Visiting")
exit()
