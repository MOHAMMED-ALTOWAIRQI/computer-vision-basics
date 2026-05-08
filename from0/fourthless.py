#changing the size of photos
import cv2
img = cv2.imread('imagesforacv\car.jpg')
new_img = cv2.resize(img,(500,500))
cv2.imshow('car',new_img)
cv2.waitKey(0)

