import cv2
import numpy as np
import pytessaract

def nothing(x):
    pass


cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
cv2.createTrackbar('hueLower','Trackbars',50,179,nothing)
cv2.createTrackbar('hueHigher','Trackbars',100,179,nothing)
cv2.createTrackbar('hueLower_2','Trackbars',50,179,nothing)
cv2.createTrackbar('hueHigher_2','Trackbars',100,179,nothing)
cv2.createTrackbar('satLower','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigher','Trackbars',255,255,nothing)
cv2.create_trackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

while True:
    ret, frame = cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    hueLow=cv2.getTrackarPos('hueLower','Trackbars')
    hueUp=cv2.getTrackarPos('hueHigher','Trackbars')

    hueLow_2=cv2.getTrackarPos('hueLower_2','Trackbars')
    hueUp_2=cv2.getTrackarPos('hueHigher_2','Trackbars')

    Ls=cv2.getTrackarPos('satLower','Trackbars')
    Us=cv2.getTrackarPos('satHigher','Trackbars')

    valL=cv2.getTrackarPos('valLow','Trackbars')
    valH=cv2.getTrackarPos('valHigh','Trackbars')

    lowerBound=np.array([hueLow,Ls,valL])
    upperBound=np.array([hueUp,Us,valH])

    lowerBound_2=np.array([hueLow_2,Ls,valL])
    upperBound_2=np.array([hueUp_2,Us,valH])

    

    FGmask=cv2.inRange(hsv,lowerBound,upperBound)
    FGmask2=cv2.inRange(hsv,lowerBound_2,upperBound_2)
    FGmaskComp=cv2.add(FGmask,FGmask2)

    x,y,w,h=0
    _,contours,_=cv2.findCountours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=50:
            cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),3)
            
            

    img=frame[x:x+w,y:y+h]
    img=cv2.cvtColor(img,cv2.CLOLOR_BGR2RGB)
    boxes=pytessaract.image.image_to_boxes(img)
    for b in boxes.splitlines():
        b=b.split(' ')
        _x,_y,_w,_h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img,(_x,h-_y),(_w,h-_h),(0,0,255),2)
        cv2.putText(img,b[0],(_x,h-_y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

    cv2.cvtColor(img,cv2.CLOLOR_RGB2BGR)
    cv2.add(frame,img)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
