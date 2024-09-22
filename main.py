import cv2
import pickle
import numpy as np
import cvzone


cap = cv2.VideoCapture("assets/carPark.mp4")

with open('assets/positions.pkl', 'rb') as f:
    posList = pickle.load(f)

width, height = 106, 48

def checkParckingSpace(imgProcessed):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCropped = imgProcessed[y:y+height, x:x+width]
        totalPixels = cv2.countNonZero(imgCropped)
        if totalPixels < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(img, f"Available: {spaceCounter}/{len(posList)}", (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    imgDilation = cv2.dilate(imgMedian, np.ones((3, 3), np.uint8), iterations=1)

    checkParckingSpace(imgDilation)
    
    
    cv2.imshow("Image", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break