import cv2
img=cv2.imread('d:/facedetect/images/k1.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier('D:/facedetect/haarcascades/Haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('D:/facedetect/haarcascades/Haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('D:/facedetect/haarcascades/Haarcascade_smile.xml')
faces=face_cascade.detectMultiScale(gray_img,1.1,9)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray=gray_img[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    #eyes
    eyes=eye_cascade.detectMultiScale(roi_gray,1.2,9)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    #smile
    smiles=smile_cascade.detectMultiScale(roi_gray,scaleFactor=1.3,minNeighbors=20)
    for(sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
cv2.imshow("Faces,Eyes, Smile",img)
cv2.waitKey(0)