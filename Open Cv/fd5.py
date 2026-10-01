import cv2
face_cascade=cv2.CascadeClassifier("D:/facedetect/haarcascades/Haarcascade_frontalface_default.xml")
image=cv2.imread("d:/facedetect/images/k1.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces_rect=face_cascade.detectMultiScale(gray,1.5,9)
for(x,y,w,h) in faces_rect:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(image,"Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)
cv2.imshow("Face Detection",image)
cv2.waitKey(0)