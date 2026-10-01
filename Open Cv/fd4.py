import cv2
face_cascade=cv2.CascadeClassifier('D:/facedetect/haarcascades/Haarcascade_frontalface_default.xml')
image=cv2.imread('d:/facedetect/images/k3.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.5,9)
print("Number of faces :",len(faces))