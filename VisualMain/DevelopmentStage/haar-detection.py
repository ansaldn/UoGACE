#written by : SHAHD R A F ALDAIHANI
import cv2

FC = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#i= cv2.imread('t.png')
cap = cv2.VideoCapture('t.mp4')

while cap.isOpened():
    _, img = cap.read()

    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = fC.detectMultiScale(g, 1.1, 4)

    for (x, y , w ,h) in f:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
