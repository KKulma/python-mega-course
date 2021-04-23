# numpy provides multiarray array object
# gets installed with pandas


import cv2
import numpy as np
# create a one-dimension array
n = np.arange(27)
print(n)
type(n)
# reshape 1-dim array to 3-dims
n.reshape(3, 3, 3)

# convert nested lists to arrays
l = [[1, 2, 3], [3, 2, 1], [0, 0, 0]]
type(l)

la = np.asarray(l)
type(la)

# OPEN CV

# image to numpy arrays
# 0 - grayscale, 1 - BGR (Blue, Green, red scale)
img = cv2.imread('16-numpy/smallgray.png', 0)
img

# numpy array to image
# turn white blobs to black
print(img)
img[1][2:4] = 0
img[2][2] = 0
cv2.imwrite("16-numpy/newimage.png", img)

# slicing
# pick columns
img[:, 2:4]

# iterate over the rows
for i in img:
    print(i)

# iterate over the columns
for i in img.T:
    print(i)

# iterate over the values
for i in img.flat:
    print(i)


# STACKING NUMPY ARRAYS
# stack 2 arrays horizontally
imgh = np.hstack((img, img))  # accepts a tuple of arrays

# split 2 arrays horizontally
imghs = np.hsplit(imgh, 2)  # specify how many arrays to split into
imghs[0][0][0]
# stack 2 arrays vertically
imgv = np.vstack((img, img))  # accepts a tuple of arrays
imgvs = np.vsplit(imgv, 2)  # specify how many arrays to split into
imgvs[0][0][0]
