#!/usr/bin/python3

import socket

# Parameters
p_ip			= '10.40.1.10'
p_port			= 5050
p_bufferSize	= 255

def init():
	global sock

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((p_ip, p_port))

def listen():
	sock.listen(4)
	conn, addr = sock.accept()

	data = conn.recv(c_bufferSize)
	print("Recived: " + str(data))
	conn.send(bytes("8", 'utf-8'))
	conn.close()

init()
while True:
	listen()
