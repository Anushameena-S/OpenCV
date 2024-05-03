from facial_emotion_recognition import EmotionRecognition
import urllib.request
import cv2
import numpy as np
import imutils

er=EmotionRecognition(device='cpu')

url='http://192.168.1.2:8080/shot.jpg'

while True:
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()), dtype=np.uint8)
    frame=cv2.imdecode(imgNp, -1)

    frame=er.recognise_emotion(frame,return_type='BGR')
    
    frame=imutils.resize(frame,width=600)
    cv2.imshow("Frame",frame)
    if ord('q')==cv2.waitKey(1):
        exit(0)
##    key=cv2.waitKey(1)
##    if key == ord('q'):
##        break
##cam.release()
##cv2.destroyAllWindows()
