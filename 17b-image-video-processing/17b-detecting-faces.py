#### face recognition
# based on the training data you can create a set of features characterising human faces, i.e. haarcascades
# here they are saved as xml files
# https://github.com/opencv/opencv/tree/4.x/data/haarcascades - haarcascades for faces

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_img = cv2.imread('news.jpg')
face_img_bw = cv2.imread('news.jpg', 0)

faces = face_cascade.detectMultiScale(face_img,
                                      scaleFactor=1.1,  # the smaller percentage over 100% the higher accuracy
                                      minNeighbors=10   # not very well explained, read the docs
                                      )

print(faces) # dimensions defining a rectagle containing a face

# draw the rectagle containing a face in the original image

for x, y, w, h in faces:
    img = cv2.rectangle(face_img,
                        (x,y), # coordinates for the top left corner
                        (x+w, y+h), # coordinates for the bottom right corner
                        (0, 255, 0), # RGB for the color (green)
                        3) # width of the rectangle

cv2.imshow("Rec", img)
cv2.waitKey(6000)
cv2.destroyAllWindows()