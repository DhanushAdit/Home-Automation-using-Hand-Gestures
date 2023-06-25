import cv2 as cv
import time
import serial
from cvzone.HandTrackingModule import HandDetector

# for serial communication
arduino = serial.Serial(port = 'COM7', timeout=0)
cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
cap.set(3, 640)
cap.set(4, 480)
tipid = [4, 8, 12, 16, 20]
while True:
    isTrue, img = cap.read()
    __, img = detector.findHands(img)
    lmlist = detector.findHands(img, draw=False)
    # print(lmlist)
    hnd = []
    l = []
    for i in lmlist:
        l = i['lmList']
        if (l[4][0] > l[3][0]):  # for thumb
            hnd.append(0)
        else:
            hnd.append(1)
        if (l[8][1] > l[6][1]):  # for index finger
            hnd.append(0)
        else:
            hnd.append(1)
        if (l[12][1] > l[10][1]):  # for middle finger
            hnd.append(0)
        else:
            hnd.append(1)
        if (l[16][1] > l[14][1]):  # for ring finger
            hnd.append(0)
        else:
            hnd.append(1)
        if (l[20][1] > l[14][1]):  # for little finger
            hnd.append(0)
        else:
            hnd.append(1)
        print(hnd)
        sum = 0
        for i in hnd:
            sum = sum + i
        print(sum)
        arduino.write(str.encode(str(sum)))
        print("summa")
    cv.imshow("img", img)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


