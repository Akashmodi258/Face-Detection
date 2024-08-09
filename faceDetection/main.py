import time
import cv2 
import mediapipe as mp
print("heloowporld")
cap=cv2.VideoCapture(0)
ptime=0
while True:
    success, img=cap.read()
    cTime = time.time()
    
    fps=1/(cTime-ptime)
    ptime=cTime
    cv2.putText(img,f'fps : {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
    cv2.imshow("image",img)
    cv2.waitKey(1)
    # hi