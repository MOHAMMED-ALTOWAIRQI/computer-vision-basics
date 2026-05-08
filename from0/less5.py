#changing colors to gray 
import cv2
img = cv2.imread('imagesforacv/animal.png')
img = cv2.resize(img,(500,500)) 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('animal',gray)
cv2.waitKey(0)