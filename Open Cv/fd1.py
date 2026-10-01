
import cv2 
img = cv2.imread('d:/facedetect/images/actor.jpg') 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

haar_cascade = cv2.CascadeClassifier('D:/facedetect/haarcascades/Haarcascade_frontalface_default.xml') 

faces_rect = haar_cascade.detectMultiScale(gray_img, 1.5, 9) 

for (x, y, w, h) in faces_rect: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
  
cv2.imshow('Detected faces', img) 
cv2.waitKey(0) 