import cv2 
vid = cv2.VideoCapture(r'C:\Users\moham\Desktop\from0\VIDEOS FOR CVS\video1.mp4')
while True:
  ret , frame = vid.read()
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  size = cv2.resize(gray,(400,300))
  cv2.imshow('video',size)   
  if cv2.waitKey(1) & 0xff == ord('q') :
    break
