from imutils import face_utils, rotate_bound
from matplotlib import pyplot
import cv2, math, argparse, imutils, numpy, dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("filters/shape_predictor_68_face_landmarks.dat") 
video = cv2.VideoCapture(0)
cv2.imshow('Video', numpy.empty((5,5),dtype=float))

f = cv2.CascadeClassifier('./filters/haarcascade_frontalface_default.xml')
e = cv2.CascadeClassifier('./filters/haarcascade_eye.xml')
m = cv2.CascadeClassifier('./filters/Mouth.xml')
n = cv2.CascadeClassifier('./filters/Nose.xml')


while True:
    ok, frame = video.read()

    if ok == False:
    	break
    # end

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output = cv2.GaussianBlur(frame, (27,27), 0)

    #detect haar features
    rects = detector(gray, 0)
    for rect in rects:
        x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()

        #copy the original version of the face into the modified output
        output[y:y+h,x:x+w,:] = frame[y:y+h,x:x+w,:]
        cv2.rectangle(output, (x, y), (x+w, y+h), (250,0,0), 2) 

        #detect eyes, but do not blur
        eyes = e.detectMultiScale(gray[y:y+h,x:x+w], scaleFactor=1.3, minNeighbors=10, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x2, y2, w2, h2) in eyes:
            cv2.rectangle(output, (x+x2, y+y2), (x + x2+w2, y + y2+h2), (0,250,250), 2)
        #end

        #detect nose, but do not blur
        nose = n.detectMultiScale(gray[y:y+h,x:x+w], scaleFactor=1.3, minNeighbors=8, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x2, y2, w2, h2) in nose:
            cv2.rectangle(output, (x+x2, y+y2), (x + x2+w2, y + y2+h2), (0,0,250), 2)
        #end

        #detect mouth, but do not blur
        mouth = m.detectMultiScale(gray[y+int(h/2):y+int(h/2)+h,x:x+w], scaleFactor=1.3, minNeighbors=10, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x2, y2, w2, h2) in mouth:
            cv2.rectangle(output, (int(x+x2), int(y+h/2+y2)), (int(x + x2+w2), int(y+h/2+y2+h2)), (0,250,0), 2) 
        #end

        #find the facial landmarks and mark them
        parts = predictor(gray, rect).parts()
        for part in parts:
            cv2.circle(output, (part.x, part.y), 1, (0, 0, 255), -1)
        #end
    #end

    cv2.imshow('output', output)

    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break;
    #end
#end


video.release()
cv2.destroyAllWindows()