import cv2
img=cv2.imread("Helloimage.jpg")
cv2.imshow('Show', img)
#cv2.imwrite('photo.png',img)

cv2.waitKey(10000)
cv2.destroyAllWindows()
