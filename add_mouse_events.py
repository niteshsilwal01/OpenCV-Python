import cv2
import numpy as np

def add_events(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        strXY=str(x)+ ','+str(y)
        cv2.putText(img,strXY,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1,cv2.LINE_AA)
        cv2.imshow('IMAGE',img)

    if events==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        print(blue ,',' ,green ,',', red)
        strBGR=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strBGR,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),1,cv2.LINE_AA)
        cv2.imshow('IMAGE',img)

#img=np.zeros([255,255,3],np.uint8)
img=cv2.imread('messi5.jpeg',1)
cv2.imshow('IMAGE',img)

cv2.setMouseCallback('IMAGE',add_events)

cv2.waitKey(0)
cv2.destroyAllWindows()