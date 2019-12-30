# OrangePI_WIn Blink 5 LEDs S Stering 5 GPIO for Leds in Python


import os
import time
os.system("echo 37 > /sys/class/gpio/export")
os.system("echo 37 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio37/direction")
os.system("echo 38 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio38/direction")
os.system("echo 39 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio39/direction")
os.system("echo 101 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio101/direction")
os.system("echo 36 > /sys/class/gpio/export")
os.system("echo out > /sys/class/gpio/gpio36/direction")
#variables
sl ="sleep 0.5"

y = 0.2
z = 0.1


L1_On = "echo 1 > /sys/class/gpio/gpio37/value"
L1_Off = "echo 0 > /sys/class/gpio/gpio37/value"
L2_On = "echo 1 > /sys/class/gpio/gpio38/value"
L2_Off = "echo 0 > /sys/class/gpio/gpio38/value"
L3_On = "echo 1 > /sys/class/gpio/gpio39/value"
L3_Off = "echo 0 > /sys/class/gpio/gpio39/value"
L4_On = "echo 1 > /sys/class/gpio/gpio101/value"
L4_Off = "echo 0 > /sys/class/gpio/gpio101/value"
L5_On = "echo 1 > /sys/class/gpio/gpio36/value"
L5_Off = "echo 0 > /sys/class/gpio/gpio36/value"

while True:##blink 5 led with speed (y)
	timeout = time.time() + 5 # 5 seconds
	while True: 
	
	
		print ("1 prog")
		os.system(L1_On)
		os.system(L2_On)
		os.system(L3_On)
		os.system(L4_On)
		os.system(L5_On)
		time.sleep (y)
		os.system(L1_Off)
		os.system(L2_Off)
		os.system(L3_Off)
		os.system(L4_Off)
		os.system(L5_Off)
		time.sleep (y)
		if time.time() > timeout:
			break
			continue
	#blink 5 led with speed (z)
	timeout = time.time() + 5 # 5 seconds	
	while True: 
	
		print ("2 prog")
		os.system(L1_On)
		os.system(L2_On)
		os.system(L3_On)
		os.system(L4_On)
		os.system(L5_On)
		time.sleep (z)
		os.system(L1_Off)
		os.system(L2_Off)
		os.system(L3_Off)
		os.system(L4_Off)
		os.system(L5_Off)
		time.sleep (z)
		if time.time() > timeout:
			break
			continue
	#right left blink		
	timeout = time.time() + 5 # 5 seconds	

	while True :
		print ("3 prog")
		os.system(L1_On)
		time.sleep (z)
		os.system(L1_Off)
		#os.system(sl)
		os.system(L2_On)
		time.sleep (z)
		os.system(L2_Off)
		#os.system(sl)
		os.system(L3_On)
		time.sleep (z)
		os.system(L3_Off)
		#os.system(sl)
		os.system(L4_On)
		time.sleep (z)
		os.system(L4_Off)
		#os.system(sl)
		os.system(L5_On)
		time.sleep (z)
		os.system(L5_Off)
		#os.system(sl)
		os.system(L4_On)
		time.sleep (z)
		os.system(L4_Off)
		#os.system(sl)
		os.system(L3_On)
		time.sleep (z)
		os.system(L3_Off)
		#os.system(sl)
		os.system(L2_On)
		time.sleep (z)
		os.system(L2_Off)
		#os.system(sl)
		if time.time() > timeout:
			break
			continue
#middle outside 
	timeout = time.time() + 5 # 5 seconds	
	while True: 
	
		print ("4 prog")
		os.system(L3_On)
		time.sleep (y)
		os.system(L2_On)
		os.system(L4_On)
		time.sleep (y)
		os.system(L5_On)
		os.system(L1_On)
		time.sleep (y)
		os.system(L1_Off)
		os.system(L2_Off)
		os.system(L3_Off)
		os.system(L4_Off)
		os.system(L5_Off)
		time.sleep (y)
		if time.time() > timeout:
			break
			continue
		
#left follow
	timeout = time.time() + 5 # 5 seconds	
	while True: 
	
		print ("5 prog")
		os.system(L1_On)
		time.sleep (z)
		os.system(L1_Off)
		#time.sleep (y)
		os.system(L2_On)
		time.sleep (z)
		os.system(L2_Off)
		#time.sleep (y)
		os.system(L3_On)
		time.sleep (z)
		os.system(L3_Off)
		#time.sleep (y)
		os.system(L4_On)
		time.sleep (z)
		os.system(L4_Off)
		#time.sleep (y)
		os.system(L5_On)
		time.sleep (z)
		os.system(L5_Off)
		#time.sleep(y)
		if time.time() > timeout:
			break
			continue
#right follow
	timeout = time.time() + 5 # 5 seconds	
	while True: 
	
		print ("6 prog")
		os.system(L5_On)
		time.sleep (z)
		os.system(L5_Off)
		#time.sleep (y)
		os.system(L4_On)
		time.sleep (z)
		os.system(L4_Off)
		#time.sleep (y)
		os.system(L3_On)
		time.sleep (z)
		os.system(L3_Off)
		#time.sleep (y)
		os.system(L2_On)
		time.sleep (z)
		os.system(L2_Off)
		#time.sleep (y)
		os.system(L1_On)
		time.sleep (z)
		os.system(L1_Off)
		#time.sleep(y)
		if time.time() > timeout:
			break
			continue

