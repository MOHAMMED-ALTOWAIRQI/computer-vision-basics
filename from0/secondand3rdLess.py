import cv2 
img = cv2.imread(r'C:\Users\moham\Desktop\from0\imagesforacv\car.jpg')
pixels = img.size
dimesions = img.shape
print("number of pixels",pixels)
cv2.imshow('car',img)
print("dimesions",dimesions)
cv2.waitKey(0)