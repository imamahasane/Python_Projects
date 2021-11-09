import cv2
import numpy as np
import pyautogu

cap = cv2.VideoCapture(0)

yello_lower = np.array([22, 93, 0])
yello_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yello_lower, yello_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0, 555, 0), 2)

    for c in contours:
        area = cv2.contourArea(c)

        if area > 300:
            #print(area)
            #cv2.drawContours(frame, c, -1, (0, 555, 0), 2)
            x, y, h, w = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 555, 0), 2)

            if y < prev_y:
                pyautogu.press("space")

            prev_y = y

    #cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(10) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
