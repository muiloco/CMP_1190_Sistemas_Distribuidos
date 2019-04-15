# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:51:41 2019

@author: Fernando R
"""

import socket
import threading               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
msg = 'Thank you for connecting'

s.listen(5)

def conexao(x):
    print(x)
    while True:     # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        c.send(msg.encode('utf-8'))
        c.close()                # Close the connection
        
threading._start_new_thread(conexao,('1'))