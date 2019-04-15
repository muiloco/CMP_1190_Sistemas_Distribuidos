# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:52:37 2019

@author: Fernando R
"""
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
msg = s.recv(1024)
print (msg)
s.close()                  
