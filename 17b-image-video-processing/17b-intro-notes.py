# conputer vision - acquiring and processing images (and videos)

import cv2
import os
import numpy as np
print(os.getcwd())
#### load, resize, display and save images


# load images
# img_col = cv2.imread("17b-image-video-processing/galaxy.jpg")
# img_bw = cv2.imread("17b-image-vidoe-praocessing/galaxy.jpg", 0)

img_col = cv2.imread("galaxy.jpg")
img_bw = cv2.imread("galaxy.jpg", 0)

print("COLOURED IMAGE /n")
print(img_col)
print(type(img_col))
print(img_col.shape)
print(img_col.ndim)

print("BLACK AND WHITE IMAGE /n")
print(img_bw)
print(type(img_bw))
print(img_bw.shape)
print(img_bw.ndim)



# resize and  display images
# resized_img_col = cv2.resize(img_col, (500, 250)) # it essentially changes img.shape dimensions, so you could also write:

# dim1 = np.round(img_col.shape[0]/2, 0).astype("int")
# dim2 = np.round(img_col.shape[1]/2, 0).astype("int")

dim1 = int(img_col.shape[0]/2)
dim2 = int(img_col.shape[1]/2)


resized_img_col = cv2.resize(img_col, (dim1, dim2))
cv2.imshow("Galaxy", resized_img_col)
cv2.waitKey(2000) # the image will appear and spontanously disapppear after this time (ms)
# cv2.waitKey(0) # the image will appear and disapppear only after you stop Pythpn
cv2.destroyAllWindows()


cv2.imshow("Galaxy", img_col)
cv2.waitKey(2000) # the image will appear and spontanously disapppear after this time (ms)
# cv2.waitKey(0) # the image will appear and disapppear only after you stop Pythpn
cv2.destroyAllWindows()

resized_img_col = cv2.resize(img_col, (dim2, dim1))
cv2.imshow("Galaxy", resized_img_col)
cv2.waitKey(2000) # the image will appear and spontanously disapppear after this time (ms)
# cv2.waitKey(0) # the image will appear and disapppear only after you stop Pythpn
cv2.destroyAllWindows()

# save images

cv2.imwrite("resized_galaxy.jpg", resized_img_col)


#### batch image import

import cv2

#glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell (in an arbitrary order)
import glob

images=glob.glob("*.jpg") # create a list containing the image file paths (assuming theyre unzipped and glob points at their location

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
