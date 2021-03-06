import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(0)

cap.set(3,640) 
cap.set(4,480)

while True:

    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerYellow = np.array([25,70,120])
    upperYellow = np.array([30,255,255])

    lowerGreen = np.array([40,70,80])
    upperGreen = np.array([70,255,255])

    lowerRed = np.array([0,50,120])
    upperRed = np.array([10,255,255])

    lowerBlue = np.array([90,60,0])
    upperBlue = np.array([121,255,255])

    mask1 = cv2.inRange(hsv, lowerYellow,upperYellow)
    mask2 = cv2.inRange(hsv, lowerGreen, upperGreen)
    mask3 = cv2.inRange(hsv, lowerRed, upperRed)
    mask4 = cv2.inRange(hsv, lowerBlue, upperBlue)

    cnts1 = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)

    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 5000:

            cv2.drawContours(frame,[c],-1,(0,255,0),3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.rectangle(frame,(30,30),(150,150),(0,255,255),cv2.FILLED)
            cv2.putText(frame,"Yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),6)

    for c in cnts2:
        area2 = cv2.contourArea(c)
        if area2 > 5000:
            cv2.drawContours(frame,[c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.rectangle(frame,(30,30),(150,150),(0,255,0),cv2.FILLED)
            cv2.putText(frame, "Green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 6)

    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:
            cv2.drawContours(frame,[c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.rectangle(frame,(30,30),(150,150),(0,0,255),cv2.FILLED)
            cv2.putText(frame, "Red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),6)

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:
            cv2.drawContours(frame,[c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.rectangle(frame,(30,30),(150,150),(255,0,0),cv2.FILLED)
            cv2.putText(frame, "Blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 6)
      
    cv2.imshow("Hasil",frame)
    k = cv2.waitKey(5)
    if k == 27:
        break 





