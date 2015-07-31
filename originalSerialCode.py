import time
import serial
import requests

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
        
print("connected to: " + ser.portstr)

#this will store the line
line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '#':
            print("Line: ")
            print (line)
            break

        
#def post_data(user, lat, lon, temp, light, zip, test = False):
#	req = requests.get("https://data.sparkfun.com/input/aGOE6rY5mxcxX1GNnOKq?" +
#		"private_key=KEo9nBl42xsZjRg94751" +
#		"&user=" + ("test-" if test else "") + user +
#		"&latitude=" 	+ str(lat) +
#		"&longitude=" 	+ str(lon) +
#		"&temperature=" + str(temp) +
#		"&light=" 	+ str(light) +
##	)

#	return req.status_code

#for i in range (0,1):
#while True:
#    temp = get_temp();
#	post_data('kstirben',40.863844,-81.446445,temp,value,'44720',True);

ser.close()

