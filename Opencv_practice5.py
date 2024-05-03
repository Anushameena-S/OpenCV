import cv2
img=cv2.imread("Helloimage.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dst=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]

thresholdImg=cv2.threshold(grayImg,131,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Original", img)
cv2.imshow("Threshold.jpg", thresholdImg)
cv2.imwrite("ThresholdImage.jpg", thresholdImg)

## 0 - Black
#180 -Mid
#255 - White
