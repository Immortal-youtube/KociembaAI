import cv2
import color_detector
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # print(check) #prints true as long as the webcam is running
    # print(frame) #prints matrix values of each framecd \
    rect = cv2.rectangle(frame, (100, 100), (150, 150), (255, 255, 255),0)
    rect2  = cv2.rectangle(frame, (200,100), (250, 150), (255, 255, 255),0)
    rect3 = cv2.rectangle(frame, (300, 100), (350, 150), (255, 255, 255),0)
    rect4 = cv2.rectangle(frame, (100, 200), (150, 250), (255, 255, 255),0)
    rect5 = cv2.rectangle(frame, (200, 200), (250, 250), (255, 255, 255),0)
    rect6 = cv2.rectangle(frame, (300, 200), (350, 250), (255, 255, 255),0)
    rect7 = cv2.rectangle(frame, (100, 300), (150, 350), (255, 255, 255),0)
    rect8 = cv2.rectangle(frame, (200, 300), (250, 350), (255, 255, 255),0)
    rect9 = cv2.rectangle(frame, (300, 300), (350, 350), (255, 255, 255), 0)
    
    # cv2.imshow("Capturing", gray)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break