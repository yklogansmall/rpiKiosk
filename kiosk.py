#!/usr/bin/python3

import pygame
import time
import csv

# Parameters
bpath		= "/home/pi/RPiKiosk/"
imgpath		= bpath+"images/"

# Globals
p_id		= 0
p_group		= "null"
p_server	= "null"
p_uname		= "null"
p_paswd		= "null"
images 		= [] # Array of [image, display time]
# screen		= pygame.display.set_mode((1280,960))#, pygame.FULLSCREEN)



############################
#         Functions        #
############################

# Read from the configuration file
def loadConfiguration():
	with open("%s.config" % (bpath), 'r') as configfile:
		reader = csv.reader(configfile, delimiter="=")
		for config in reader:
			param = config[0].strip()
			value = config[1].strip()

			if param == "id":
				p_id = int(value)
			if param == "group":
				p_group = value
			if param == "server":
				p_server = value
			if param == "uname":
				p_uname = value
			if param == "paswd":
				p_paswd = value


# Check to see if updates exist on the control server, and if they
# do, download them
def update():
	pass

# Connect to control server, let it know who you are, where you are
# and what you're all about
def bonjour():
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

loadConfiguration()
print(p_id)
print(p_paswd)
exit()

loadImages()
while True:
	dispImages()
