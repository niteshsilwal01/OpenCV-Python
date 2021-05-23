import cv2
import numpy as np

#img=np.zeros([512,512,3],np.uint8)
img=cv2.imread('mango.jpeg',1)
cv2.imshow("IMAGE",img)

def mouse_events(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        
        #show another window representing the color clicked by mouse
        color_img=np.zeros([512,512,3],np.uint8)
        color_img[:]=[blue, green, red]
        cv2.imshow("COLOR",color_img)
     
cv2.setMouseCallback("IMAGE",mouse_events)
cv2.waitKey(0)
cv2.destroyAllWindows()