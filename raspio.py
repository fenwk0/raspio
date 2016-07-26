from random import randint

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# See this website for sundounder BCM
# http://heinrichhartmann.com/2014/11/22/Raspberry-Pi-SunFounder-GPIO-Layout.html

#GPIO0	GPIO17
#GPIO1	GPIO18
#GPIO2	GPIO21

#GPIO.setup(17,GPIO.OUT)
#print "LED on"
#GPIO.output(17,GPIO.HIGH)
#time.sleep(1)
#print "LED off"
#GPIO.output(17,GPIO.LOW)

#GPIO.setup(18,GPIO.OUT)
#print "LED on"
#GPIO.output(18,GPIO.HIGH)
#time.sleep(1)
#print "LED off"
#GPIO.output(18,GPIO.LOW)

#GPIO.setup(27,GPIO.OUT)
#print "LED on"
#GPIO.output(27,GPIO.HIGH)
#time.sleep(1)
#print "LED off"
#GPIO.output(27,GPIO.LOW)


def randomTine():
   return randint(0,9);

def light(  pin, sleep ):
   GPIO.setup(pin,GPIO.OUT)
   print "LED on"
   GPIO.output(pin,GPIO.HIGH)
   time.sleep(sleep)
   print "LED off"
   GPIO.output(pin,GPIO.LOW)
   return;

while True:

   light( 17, 1)
   light( 18, 1)
   light( 27, 1)

