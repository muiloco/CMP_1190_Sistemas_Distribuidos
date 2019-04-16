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
    m, server = servidor.recv(1024)
    print(server,str(m, 'utf-8'))
    servidor.send(msg.encode('utf-8'))
    msg = input()
servidor.close()