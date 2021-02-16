
import cv2
import numpy as np
import pytesseract
import threading

#HSV scheme for yellow-orange number plates:
#0
#30
#max
#0
#150
#max
#150
#max

def nothing(x):
    pass

count=0

AS_VAL=250

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',350,300)
cv2.createTrackbar('hueLower','Trackbars',50,179,nothing)
cv2.createTrackbar('hueHigher','Trackbars',100,179,nothing)
cv2.createTrackbar('hueLower_2','Trackbars',50,179,nothing)
cv2.createTrackbar('hueHigher_2','Trackbars',100,179,nothing)
cv2.createTrackbar('satLower','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigher','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)
cv2.namedWindow('newCam')
cv2.namedWindow('ROI')
cv2.namedWindow('newCam')
dispW=320
dispH=240
flip=0 #set 2 for a acamera facing straight 

(X1,Y1,H1,W1,area1)=(20,20,20,20,0)#ROI defaultSize

def textRecogThreading(roi,area1):
    while area1>=(AS_VAL-(AS_VAL*0.15)):
        temp_Roi=cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
        text=pytesseract.image_to_string(temp_Roi,lang='eng',config='--psm 6')
        if(not(text.isspace())):
            print("The license plate states: ")
            print(text)
        area1=0

def displayFn(roi,FGmaskComp,frame):
    cv2.imshow('newCam',FGmaskComp)
    cv2.moveWindow('newCam',0,300)
    cv2.imshow('ROI',roi)
    cv2.moveWindow('ROI',350,0)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    
    



#width=3264, height=2464
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=30/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)



while True:
    ret, frame = cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    hueLow=cv2.getTrackbarPos('hueLower','Trackbars')
    hueUp=cv2.getTrackbarPos('hueHigher','Trackbars')

    hueLow_2=cv2.getTrackbarPos('hueLower_2','Trackbars')
    hueUp_2=cv2.getTrackbarPos('hueHigher_2','Trackbars')

    Ls=cv2.getTrackbarPos('satLower','Trackbars')
    Us=cv2.getTrackbarPos('satHigher','Trackbars')

    valL=cv2.getTrackbarPos('valLow','Trackbars')
    valH=cv2.getTrackbarPos('valHigh','Trackbars')

    lowerBound=np.array([hueLow,Ls,valL])
    upperBound=np.array([hueUp,Us,valH])

    lowerBound_2=np.array([hueLow_2,Ls,valL])
    upperBound_2=np.array([hueUp_2,Us,valH])

    

    FGmask=cv2.inRange(hsv,lowerBound,upperBound)
    FGmask2=cv2.inRange(hsv,lowerBound_2,upperBound_2)
    FGmaskComp=cv2.add(FGmask,FGmask2)

    
    contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=AS_VAL:
            cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),3)
            X1=x
            Y1=y
            H1=h
            W1=w
            area1=area
    count=count+1
    roi=frame[Y1:Y1+H1,X1:X1+W1]
    if count==(AS_VAL*2):
        t1=threading.Thread(target=textRecogThreading, args=(roi,area1))
        t1.start()
        t1.join()
        count=0
    t2=threading.Thread(target=displayFn, args=(roi,frame,FGmaskComp))
    
    t2.start()
    
    t2.join()
    
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

