#!/usr/bin/env python3
import os
import requests

text_files_location = '/data/feedback/'

for filename in os.listdir(text_files_location):
	print(filename)
