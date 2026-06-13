import cv2
import numpy as np
#STORING THE IMAGE 
img = cv2.imread('data.png')

#COLOURED IMAGE TO GREY IMAGE
img_grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#PLAYING WITH BGR

img_blue = img[:,:,0]
img_green = img[:,:,1]
img_red = img[:,:,2]

new_image = np.hstack((img_blue,img_green ,img_red))


#RESIZE
img_resize = cv2.resize(img,(300,300))

#FLIP 
img_vert_flip = cv2.flip(img,0)
img_hori_vert_flip = cv2.flip(img,-1)
img_hori_flip = cv2.flip(img,1)


#DISPLAYING THE IMAGE
cv2.imshow('window', img_hori_vert_flip)

#TIME TO BE DISPLAYED IN SCREEN
cv2.waitKey(0)
 

