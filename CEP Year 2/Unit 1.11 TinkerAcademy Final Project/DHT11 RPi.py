'''This file was used by the Raspberry Pi to measure
Temperature and Humidity using the DHT11 sensor
and to display values on the 7 segment LED'''
#--------------SETUP---------------
import RPi.GPIO as GPIO
import thingspeak
import time
import Adafruit_DHT as DHT
from Adafruit_LED_Backpack import SevenSegment as SS

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

temphumidpin = 25
GPIO.setup(temphumidpin,GPIO.IN)

segment = SS.SevenSegment(address = 0x70)
segment.begin()

templist = []
humidlist = []
channel = thingspeak.Channel(311611,
                             api_key = 'IU84FZDLGICE1DO9',
                             write_key = '60O2D4K3Y7ONXFSG')

def temphumidity(repeattime):
    seg = 0
    if repeattime < 3:
        repeattime = 3.5
        #This makes sure the sensor has the buffer time needed (so it cannot melt).
        
#--------TEMP AND HUMIDITY DATA COLLECTION-----------
    while True:
        hum, temp = DHT.read_retry(DHT.DHT11, temphumidpin)
        #DHT11 sensor measures temp and humidity data.
        if temp is not None and hum is not None:
            print('Temperature =', temp)
            print('Humidity =', hum)
            templist.append(temp)
            humidlist.append(hum)
            
#--------TEMP AND HUMIDITY DATA UPLOAD TO THINGSPEAK SERVER-----
            uploaddata = {1:temp,2:'{:.2f}'.format(sum(templist)/len(templist)),3:hum,4:'{:.2f}'.format(sum(humidlist)/len(humidlist))}
            channel.update(uploaddata)
            #Data is uploaded to server.
            seg = 1
        else:
            print('Failed to get reading')
            
#---------FEATURE: 7 SEGMENT LED-------------
        if seg == 1:
            segment.set_colon(True)
            segment.set_digit(0,7)
            segment.set_digit(1,'E')
            #7 and E meant to simulate TE(for Temperature).
            segment.set_digit(2,int(str(temp)[0]))
            segment.set_digit(3,int(str(temp)[1]))
            #Shows temp data for ~1/2 the time
            segment.write_display()
            time.sleep(repeattime/2 + 0.5)
            segment.set_digit(0,1)
            segment.set_digit(1,'D')
            #1 and D on the display meant to simulate the unsupported letter H(for Humidity).
            segment.set_digit(2,int(str(hum)[0]))
            segment.set_digit(3,int(str(hum)[1]))
            #Shows humidity data for ~1/2 the time
            segment.write_display()
            time.sleep(repeattime/2 - 0.5)
        else:
            time.sleep(repeattime)
            
        segment.clear()
        seg = 0

temphumidity(20)
            

        
