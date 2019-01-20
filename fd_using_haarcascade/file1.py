import cv2


#colored image
img = cv2.imread("Priyanka.jpg",1)

resized = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))

#Black and White (Gray Scale)
#img_1 =cv2.imread ("Priyanka.jpg",0)

#print(img.shape, img_1.shape)

cv2.imshow("Priyanka", resized)
#cv2.waitKey(0)

cv2.waitKey(2000)

cv2.destroyAllWindows()
