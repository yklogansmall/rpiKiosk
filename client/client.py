#!/usr/bin/python3

import pygame
import time
import csv
import socket
import os.path
import uuid

# Parameters
p_group			= "dev"
p_server		= "10.40.1.10"
p_port			= 5050
p_p_bufferSize	= 255
# Constants
bpath		= "/home/pi/rpiKiosk/"
imgpath		= bpath+"images/"
images 		= [] # Array of [image, display time]


############################
#         Methods          #
############################

def getUUID():
	global g_UUID
	if os.path.exists(bpath+".uuid"):
		with open(bpath+".uuid", 'r') as file:
			g_UUID = file.read()
	else:
		with open(bpath+".uuid", 'w') as file:
			g_UUID = str(uuid.uuid4())
			file.write(g_UUID)

def initPygame():
	global screen
	screen = pygame.display.set_mode((1280,960))#, pygame.FULLSCREEN)

# Connect to the control server, let it know what group you belong to and obtain a unique identifier
def getID():
	global g_id
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((p_server, p_port))
	
	sock.send(bytes("getid %s %s"%(p_group, g_UUID), 'utf-8'))
	g_id = int(sock.recv(p_bufferSize).decode('utf-8'))

# Check the control server for new images to display. If they exist, download them.
# Should be run every minute
def update():
	pass

def loadImages():
	i = 0
	with open("%smanifest.csv" % (imgpath), 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			images.append([pygame.image.load(imgpath + row[0]), row[1]])

def dispImages():
	for image in images:
		screen.blit(image[0], (0, 0))
		pygame.display.flip()
		time.sleep(int(image[1]))

############################
#       Main Program       #
############################

print("RPi Kiosk")
print("By Logan Small")

# Init
getUUID()
getID()
loadImages()
initPygame()

# Main Loop
while True:
	dispImages()
