import cv2
#import numpy as np

cv2.namedWindow('Image')

def change_value(x):
    print(x)

cv2.createTrackbar('Position','Image',22,121,change_value)
cv2.createTrackbar('Color/Gray','Image',0,3,change_value)

while(True):
    img=cv2.imread('mango.jpeg',1)
    pos=cv2.getTrackbarPos('Position','Image')
    cv2.putText(img,str(pos),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),10,cv2.LINE_8)

    if cv2.waitKey(1)==27:
        break

    switch=cv2.getTrackbarPos('Color/Gray','Image')
    if switch==0:
        pass
    elif switch==1:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif switch==2:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)
    cv2.imshow('Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
