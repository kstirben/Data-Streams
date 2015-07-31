import time
import serial
import requests
import re

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
        
print("connected to: " + ser.portstr)

while 1:

    #this will store the line
    line = []

    OK = 1;

    while OK == 1:
        for c in ser.read():
            line.append(c)
            if c == '#':
                #            print("Line: ")
                #            print (line)
                OK = 0
                break
        
        str = "";
        seq = (line); # This is sequence of strings.
        newline = str.join( seq );
        #print ("newline: ");
        #print (newline);

    words = " ";
    wordlist = [];
    newlist = [None] * 8;
    i = 0;

    for x in newline:
        if x != '#' and x != ",":    
            words = words + x
        else:
            newlist[i] = words
            i += 1
            words = " "
        
        # newlist(0) = wind mph
        # newlist(1) = wind direction
        # newlist(2) = humidity
        # newlist(3) = temperature fahrenheit
        # newlist(4) = pressure
        # newlist(5) = light_level
        # newlist(6) = blank
        # newlist(7) = none

    tempc = 0.0;
    tempf = float(newlist[3]);
    tempc = (tempf - 32) / 1.8;
    tempcst = "%.2f" % tempc;
    light_lvl = newlist[5];
    print light_lvl;
    
    for i in range(0,1):
        #while True:
        req = requests.get("https://data.sparkfun.com/input/aGOE6rY5mxcxX1GNnOKq?" +
            "private_key=KEo9nBl42xsZjRg94751" +
            "&user=kstirben" +
            "&latitude=40.863844" 	+
            "&longitude=-81.446445" + 
            "&temperature=" + tempcst +
            "&light=" 	+ light_lvl +
            "&zip=44720"
            )

    time.sleep(300)
            
ser.close()
