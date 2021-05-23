import cv2

#Creating a method for reading and saving video
cap= cv2.VideoCapture(0)  
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output_video.avi',fourcc,20,(640,480))

while(cap.isOpened()):
    #Reading
    ret,frame = cap.read()

    #Writing frame into out
    if ret==True:

        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('Output_Frame',gray)
        
        k=cv2.waitKey(1)
        if k==27:
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()






