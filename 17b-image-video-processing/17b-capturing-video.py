import cv2
import time

# record a video: trigger the webcam, keep it on for 3 secs and then stop
video = cv2.VideoCapture()

## commented out bits not working as expected so I skipped the remaining code for recording the video live
check, frame = video.read()
# print(check)
# print(frame)

time.sleep(2)
cv2.imshow("Capturing", frame)

cv2.waitKey(2000)
video.release()
cv2.destroyAllWindows()


# video = cv2.VideoCapture('video.mov')