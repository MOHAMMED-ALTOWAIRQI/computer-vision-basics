import cv2
img = cv2.imread(r'C:\Users\moham\Desktop\from0\imagesforacv\animal.png')
print(img)
cv2.imshow('animal',img)
cv2.waitKey(0)