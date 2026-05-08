#creating two buttons one to close the imge the second to save it
import cv2
img = cv2.imread('imagesforacv/animal.png')
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('animal',gray)
k = cv2.waitKey(0)
# 27 = esc key for exit and ord('s') = s key for save the image
if k == 27 :
  cv2.destroyAllWindows
elif k ==ord('s'):
  cv2.imwrite(r"C:\Users\moham\Pictures\newanimal.png",gray)
  cv2.destroyAllWindows()
