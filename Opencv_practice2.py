import cv2

image=cv2.imread("Helloimage.jpg")
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)
cv2.imshow('GrayScale', grayImage)
cv2.imwrite('graynew.jpg',grayImage)

print(image.shape)
print(image.size)
