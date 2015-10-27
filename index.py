#!/usr/bin/python3

import os

print("Content-type: text/html\r\n\r\n")

with open('./index.html', 'r') as auth_file:
	print(auth_file.read())

exit()
