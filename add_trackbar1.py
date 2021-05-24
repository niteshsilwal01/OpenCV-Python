import cv2
import numpy as np

img=np.zeros([255,512,3],np.uint8)
cv2.namedWindow('Image')

def change_value(x):
    print(x)

cv2.createTrackbar("B",'Image',0,255,change_value)
cv2.createTrackbar("G",'Image',0,255,change_value)
cv2.createTrackbar("R",'Image',0,255,change_value)
cv2.createTrackbar("0:OFF\n1:ON",'Image',0,1,change_value)


while(True):
    cv2.imshow('Image',img)
    if cv2.waitKey(1)==ord('c'):
        break

    b=cv2.getTrackbarPos("B",'Image')
    g=cv2.getTrackbarPos("G",'Image')
    r=cv2.getTrackbarPos("R",'Image')
    switch=cv2.getTrackbarPos("0:OFF\n1:ON",'Image')
    if switch==1:
        img[:]=[b,g,r]
    else:
        img[:]=0

cv2.destroyAllWindows()



