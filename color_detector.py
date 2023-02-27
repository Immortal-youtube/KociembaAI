import cv2
import numpy as np
cap = cv2.VideoCapture(0)



def blue(frame):
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(imgHSV,lower_blue,upper_blue)
    result = cv2.bitwise_not(frame,frame,mask=mask)
    return result

# lower_green = np.array([40,30,30 ])
# upper_green = np.array([100,255,255])
# mask2=cv2.inRange(imgHSV,lower_green,upper_green)
# result2 = cv2.bitwise_and(frame,frame,mask=mask2)
# lower_white = np.array([0,0,0])
# upper_white = np.array([0,0,255])
# mask3 = cv2.inRange(imgHSV,lower_white,upper_white)
# result3 = cv2.bitwise_and(frame,frame,mask=mask3)
# lower_red = np.array([0,50,50])
# upper_red = np.array([10,255,255])
# mask4 = cv2.inRange(imgHSV,lower_red,upper_red)
# result4 = cv2.bitwise_and(frame,frame,mask=mask4)
# upper_orange = np.array([45,255,255])
# lower_orange = np.array([30,255,255])
# mask5 = cv2.inRange(imgHSV,lower_orange,upper_orange)
# result5 = cv2.bitwise_and(frame,frame,mask=mask5)
# upper_yellow = np.array([30,255,255])
# lower_yellow = np.array([25,50,50])
# mask6 = cv2.inRange(imgHSV,lower_yellow,upper_yellow)
# result6 = cv2.bitwise_and(frame,frame,mask=mask6)

