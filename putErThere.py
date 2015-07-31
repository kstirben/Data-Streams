## post_data.py
import requests
# temp2.py
import time
# analog.py
#!/usr/bin/env python
#import time
import os
import RPi.GPIO as GPIO

# analog.py
GPIO.setmode(GPIO.BCM)
DEBUG = 1

#weather.py
#import post_data
#import time

def post_data(user, lat, lon, temp, light, zip, test = False):
	req = requests.get("http://data.sparkfun.com/input/aGOE6rY5mxcxX1GNnOKq?" +
		"private_key=KEo9nBl42xsZjRg94751" +
		"&user=" + ("test-" if test else "") + user +
		"&latitude=" 	+ str(lat) +
		"&longitude=" 	+ str(lon) +
		"&temperature=" + str(temp) +
		"&light=" 	+ str(light) +
		"&zip="		+ str(zip)
	)

	return req.status_code

#temp2.py

def get_temp():
	f = open("/sys/bus/w1/devices/28-000006395840/w1_slave",'r')
	s = f.readlines()
	f.close()
	if not s[0].strip().endswith("YES"):
		return None
	else:
		t = float(s[1].split("=")[-1].strip())/1000;
		print "Temperature = ", t
	return t

#	for i in range(0,10):
#		print "Temperature = ", get_temp()
#		time.sleep(2.0)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)

        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

#for i in range(0,1):
#while True:
channel = 0
value = readadc(channel, SPICLK, SPIMOSI, SPIMISO, SPICS)
print "Light=", value
#	time.sleep(60)


# import analog
# import temp2

for i in range (0,1):
#while True:
    temp = get_temp();
	post_data('kstirben',40.863844,-81.446445,temp,value,'44720',True);
#	time.sleep(60)
