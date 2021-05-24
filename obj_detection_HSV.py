import cv2 
import numpy as np

#For placing trackbars
cv2.namedWindow("Tracker")


def change_value(x):
    print(x)

#Trackbar to change the value of H,S and V manually
cv2.createTrackbar('LH','Tracker',0,255,change_value)
cv2.createTrackbar('LS','Tracker',0,255,change_value)
cv2.createTrackbar('LV','Tracker',0,255,change_value)
cv2.createTrackbar('UH','Tracker',255,255,change_value)
cv2.createTrackbar('US','Tracker',255,255,change_value)
cv2.createTrackbar('UV','Tracker',255,255,change_value)

#Reading input from video
cap=cv2.VideoCapture(0)

while True:
    #frame=cv2.imread('mc.jpeg',1)   <<--Input can also be read from images
    _,frame=cap.read()
    
        
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos('LH','Tracker')
    ls=cv2.getTrackbarPos('LS','Tracker')
    lv=cv2.getTrackbarPos('LV','Tracker')
    uh=cv2.getTrackbarPos('UH','Tracker')
    us=cv2.getTrackbarPos('US','Tracker')
    uv=cv2.getTrackbarPos('UV','Tracker')

    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])
    
    mask=cv2.inRange(frame,l_b,u_b)

    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Video',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',result)


    if cv2.waitKey(1)==ord('c'):
        break