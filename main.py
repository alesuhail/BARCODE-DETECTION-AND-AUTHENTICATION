import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)  #video capture source

# cap.set(3,380)
# cap.set(4,480)
# check, imgs = cap.read()
# print(check)

cap.set(3, 380)
cap.set(4, 480)

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

while True:

    check, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8') # convert data to string
        print(myData)
        if myData in myDataList:
            myOutput = 'Authorized'
            Color = (255, 0, 255)
        else:
            myOutput = 'No-Authorized'
            Color = (0, 255, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, Color, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_DUPLEX, 0.9, Color, 2)

    cv2.imshow('result', img)
    cv2.waitKey(1)



