# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:52:37 2019

@author: Fernando R
"""
import socket               # Import socket module

servidor = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

servidor.connect((host, port))
print("Para sair digite: Exit")
msg = input()
while msg != 'Exit':
    m = servidor.recv(1024)
    print("Msg Server:",m)
    servidor.send(msg.encode('utf-8'))
    msg = input()
servidor.close()