#!/usr/bin/env python3
import os
import requests
import socket
import subprocess

#ipaddress = subprocess.call('var=$(curl ifconfig.me)')
#ipaddress = subprocess.call('var=$(curl ifconfig.me)',executable='/bin/bash/')
url = 'http://35.239.172.202/feedback/'
directory_text = '/data/feedback/'
dictionary = {}

for filename in os.listdir(directory_text):
	with open(directory_text + filename, 'r') as text:
		line = text.readline()
		dictionary['title'] = line
		line = text.readline()
		dictionary['name'] = line
		line = text.readline()
		dictionary['date'] = line
		line = text.readline()
		dictionary['feedback'] = line
	response = requests.post(url, data = dictionary)
	print(response.status_code)
#print(dictionary)

#ipaddress = socket.getsockname()

#print(socket.gethostbyname(socket.gethostname()))

#print(ipaddress)

