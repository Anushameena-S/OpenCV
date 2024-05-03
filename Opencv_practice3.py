import cv2
import imutils
img=cv2.imread('photo.png')
resizedImage=imutils.resize(img, width=200)
cv2.imshow('OriginalImage2', img)
cv2.imshow('Resized Image', resizedImage)
cv2.imwrite('resizedimage.jpg', resizedImage)
