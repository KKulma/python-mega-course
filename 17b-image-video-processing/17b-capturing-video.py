import cv2
import time

# record a video: trigger the webcam, keep it on for 3 secs and then stop
video = cv2.VideoCapture(0)

a = 1
while True:
    a = a+1
    check, frame = video.read()
    print(check)
    print(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BayerGR2GRAY)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()


# ### code tried earlier
#
# video = cv2.VideoCapture(0)
#
# check, frame = video.read()
# # print(check)
# # print(frame)
#
# time.sleep(2)
# cv2.imshow("Capturing", frame)
#
# cv2.waitKey(2000)
# video.release()
# cv2.destroyAllWindows()
