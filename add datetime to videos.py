import cv2
import datetime

cap=cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('outvideo.avi',fourcc,20,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        out.write(frame)
        
        font_write=cv2.FONT_HERSHEY_SIMPLEX
        date_time=str(datetime.datetime.now())
        frame=cv2.putText(frame,date_time,(10,50),font_write,0.75,(0,255,255),2)

        cv2.imshow('video',frame)
        if cv2.waitKey(1)==27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



