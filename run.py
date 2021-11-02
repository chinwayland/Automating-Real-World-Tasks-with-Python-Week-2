#!/usr/bin/env python3
import os
import requests

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
print(dictionary)
