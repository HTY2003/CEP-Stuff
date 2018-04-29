'''This file was used by the Raspberry Pi to measure Wind Speed
and operate the buzzer when the wind vanes rotated one time'''
#-----------SETUP----------
from timeit import default_timer as timer
import RPi.GPIO as GPIO
import time
import datetime
import thingspeak

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

receiverpin = 17
emitterpin = 24
buzzerpin = 8

GPIO.setup(receiverpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(emitterpin, GPIO.OUT)
GPIO.setup(buzzerpin, GPIO.OUT)

GPIO.output(emitterpin, True)

rpm = []
channel = thingspeak.Channel(340307,
                             api_key = 'I2I69J7MDBNNDQ6X',
                             write_key = 'OW7CDC2Y1HVVMVZM')
def windspeed():
    rounds = 0
    starttime = 0
    pressed = 0

    pitch = 523
    duration = 0.07
    period = 1.0/pitch
    delay = period / 2
    cycles = int(duration*pitch)
    
#-----------WIND SPEED DATA COLLECTION-----------
    while True:
        if starttime == 0:  
            starttime = round(timer())
            #This ensures that every time the data is uploaded, there is a new timer to measure from. 
        if GPIO.input(receiverpin):
            if pressed == 0:
                rounds += 1
                #When the beam is connected with the sensor, it is counted as one revolution.
                pressed = 1
                #This ensures that the rotation counter will not continuously record loops when the beam continues to connect.
                
#-----------FEATURE: ROTATION BUZZER------------- 
                for i in range(cycles):
                    #When a rotation is recorded, the buzzer beeps.
                    GPIO.output(buzzerpin,True)
                    time.sleep(delay)
                    GPIO.output(buzzerpin,False)
                    time.sleep(delay)
        else:
            pressed = 0
            # Signifies that the beam has been broken, so the next loop can be recorded.
            
#----------WIND SPEED DATA UPLOAD TO THINGSPEAK SERVER--------------
        if round(timer()) - starttime == 20:    #Records every 20 seconds
            rounds *= 3
            rpm.append(rounds)
            print('RPM: ' + str(rpm))
            uploaddata = {1:rounds, 2: '{:.2f}'.format(sum(rpm)/len(rpm))}
            channel.update(uploaddata)          #Data in RPM is uploaded to the server.
            rounds = 0
            starttime = 0                       #Stats are reset to record new loops.
           
windspeed()







