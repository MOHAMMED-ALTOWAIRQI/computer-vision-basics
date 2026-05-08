import cv2 
img = cv2.imread('imagesforacv\car.jpg')

#LINE
#cv2.line(img,(10,10),(200,10),(0,255,0),5)
#rectangle 
cv2.rectangle(img,(300,20),(600,300),(0,255,0),4)
cv2.putText(img,('car'),(300,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow('car',img)
cv2.waitKey(0)
