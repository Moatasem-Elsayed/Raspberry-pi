import cv2
import numpy as np
import random
import playsound
import os
from gtts import gTTS
import time
def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='ar')
    # tts = gTTS(text=audios, lang='en')
    r = random.randint(1, 100000000)
    audioF = 'audio' + str(r) + '.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)
capt=cv2.VideoCapture(0)

while True:
 _,frame=capt.read()
 blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
 hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
 cv2.putText(frame,"Graduation Project Screen",(150, 20 ), cv2.FONT_HERSHEY_PLAIN, 2, (128,128,0), 2)
 # Green color
 low_green =  np.array([25, 52, 72])
 high_green = np.array([102, 255, 255])
 green_mask = cv2.inRange(hsv_frame, low_green, high_green)
 #green = cv2.bitwise_and(frame, frame, mask=green_mask)
 contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
 for contour in contours:
     area=cv2.contourArea(contour)
     if area>3000:
      cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
      x, y, _, _ = cv2.boundingRect(contour)
      cv2.putText(frame, "Green", (x, y ), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
      #Bixby_Speak("القلب اخضر وسيبها على الله ")
      time.sleep(2)
 #########################################################################################

 # red color
 low_red = np.array([161, 155, 84])
 high_red = np.array([179, 255, 255])
 red_mask = cv2.inRange(hsv_frame, low_red, high_red)
#  red=cv2.bitwise_and(frame,frame,mask=red_mask) 
 contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
 for contour in contours:
     area=cv2.contourArea(contour)
     if area>1000:
      cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
      x, y, _, _ = cv2.boundingRect(contour)
      cv2.putText(frame, "red", (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
      #Bixby_Speak("احمر يا اسد الكون")
      time.sleep(2)
      
#########################################################################################
 # Blue color
 low_blue = np.array([94, 80, 2])
 high_blue = np.array([126, 255, 255])
 blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
 #blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
 contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
 for contour in contours:
     area=cv2.contourArea(contour)
     if area>3000:
      cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
      x, y, _, _ = cv2.boundingRect(contour)
      cv2.putText(frame, "Blue", (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
      #Bixby_Speak("ازرق يا ابو صحاب")
      time.sleep(2)
#########################################################################################
 cv2.imshow("Frame",frame)
#  cv2.imshow("mask",red)
#  cv2.imshow("Blue", blue)
#  cv2.imshow("Green", green)
 key=cv2.waitKey(1)
#  print ((hsv_frame))
#  break
 if key == ord('z'):
     break

capt.release()
cv2.destroyAllWindows()
