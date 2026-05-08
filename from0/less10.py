import cv2
camera = cv2.VideoCapture(0)
while True:
  ret , video = camera.read()
  newe_cam = cv2.resize(video,(400,300))
  cv2.imshow('video',newe_cam)
  if cv2.waitKey(1) & 0xff == ord('q') :
    break 