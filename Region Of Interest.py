import cv2

img=cv2.imread('messi5.jpeg',1)
roi1=cv2.selectROI(img)
print(roi1)

cr_img=img[int(roi1[1]):int(roi1[1]+roi1[3]),
           int(roi1[0]):int(roi1[0])+roi1[2]]

cv2.imshow("IMAGES",cr_img)

cv2.waitKey(0)