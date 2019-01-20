import cv2

#create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("/home/priyankasaggu119/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

#Reading the image as it is 
img = cv2.imread("Priyanka.jpg",1)

#Reading the image as grey scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the co-ordinates of the image
faces=face_cascade.detectMultiScale(gray_img, 1.3,5)

print(type(faces))
print(faces)


for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

#resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

