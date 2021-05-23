import cv2

#Reading image
img=cv2.imread('cat.webp',0)

#Display IMage
cv2.imshow('Biralo',img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):

    #Writing the Image(Copying)
    cv2.imwrite('cat_copy.jpg',img)
    cv2.destroyAllWindows()
