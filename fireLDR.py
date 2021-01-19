# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep 
import time

from firebase import firebase
import sys
sys.path
from datetime import datetime

fire=firebase.FirebaseApplication("https://test-cad72-default-rtdb.firebaseio.com/",authentication =None)
now = datetime.now()
today=datetime.today()
# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
data={

    '1-Date'  : d2,
    '2-Time'  :current_time,
    '3-LDR'  :0
}



# result=fire.post('/test-cad72-default-rtdb/profile/point2',data) #add with traditional nodes
result=fire.patch('/test-cad72-default-rtdb/profile'+'/points2',data) #add with specific nodes 
# result=fire.delete('/test-cad72-default-rtdb/profile','')#delete node
# result=fire.put('/test-cad72-default-rtdb/profile/points','3-Name','Soma')#update
print(result)

##########################################################
GPIO.setmode(GPIO.BOARD)
delayt = .1 
value = 0 # this variable will be used to store the ldr value
ldr = 7 #ldr is connected with pin number 7
led = 5 #led is connected with pin number 11
GPIO.setup(led, GPIO.OUT) # as led is an output device so that’s why we set it to output.
GPIO.output(led, False) # keep led off by default 
def rc_time (ldr):
    count = 0
 
    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)
 
    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)
 
    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1
 
    return count
 
 
#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print("Ldr Value:")
        value = rc_time(ldr)
        print(value)
        if ( value <= 10000 ):
                print("Lights are ON")
                GPIO.output(led, True)
        if (value > 10000):
                print("Lights are OFF")
                GPIO.output(led, False)
        sleep(2)
        now = datetime.now()
        today=datetime.today()
        # Textual month, day and year	
        d2 = today.strftime("%B %d, %Y")
        print("d2 =", d2)
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        result=fire.put('/test-cad72-default-rtdb/profile/points','3-LDR',value) #update
        result=fire.put('/test-cad72-default-rtdb/profile/points','2-Time',current_time) #update
        result=fire.put('/test-cad72-default-rtdb/profile/points','1-Date',d2) #update
        print(result)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
