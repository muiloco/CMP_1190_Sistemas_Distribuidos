# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:51:41 2019

@author: Fernando R
"""

import socket
import _thread               # Import socket module

class Cliente:
    cont_cliente=0
    def __init__(self, cliente, ipcliente, status):
        self.cliente = cliente
        self.ipcliente = ipcliente
        self.status = True

def conexao(con, cliente):
    print("Conectado:", cliente)
    while True:     # Now wait for client connection.
        msg = con.recv(1024)
        if not msg: break
        print(msg, cliente)
    print("Finalizado conexao:", cliente)
    con.close()
    _thread.exit()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
msg = 'Thank you for connecting'

s.listen(1)
        
while True:
    con, cliente = s.accept()
    _thread.start_new_thread(conexao, tuple([con, cliente]))

s.close()