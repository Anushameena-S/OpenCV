import cv2

# Keep this xml "haarcascade_frontalface_default.xml" in the folder
# where you run this program

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

##To detect face from a recorded and saved video
##Replace 'path/to/your/vidoe.mp4 with path to your file
##------------------------------------------------------
##video_path="check.mp4"
##cam=cv2.VideoCapture(video_path)
##
##To detect face from image
##-----------------------------
##video_path="pic.jpg"
##cam=cv2.VideoCapture(video_path)

while True:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
# Key 27 value is escape
cam.release()
cv2.destroyAllWindows()
