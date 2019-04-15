# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:51:41 2019

@author: Fernando R
"""

import socket
import _thread               # Import socket module

listaDeCliente = []


class Clientes:
    cont_cliente=0
    def __init__(self, cliente, ipcliente, status):
        self.cliente = cliente
        self.ipcliente = ipcliente
        self.status = status
    
    def imprimir(self):
        print("Cliente:", self.ipcliente)

def conexao(con, cliente, qnt_clientes):
    print("Conectado:", cliente) 
    while True:     # Now wait for client connection.
        msg = con.recv(1024)
        if not msg: break
        print(msg, cliente)
    print("Finalizado conexao:", cliente)
    con.close()
    _thread.exit()

def ListaDeClientes(objCliente):
    listaDeCliente.append(objCliente)

def imprimirListaCliente():
    n = len(listaDeCliente)
    x=0
    while x < n:
        cliente = listaDeCliente[x]
        cliente.imprimir()
        x+=1


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
msg = 'Thank you for connecting'

s.listen(1)

qnt_clientes = input("Insira a quantidade de clintes a serem usado:\n")
qnt_clientes = int(qnt_clientes)
n = 0

while True:
    if n < qnt_clientes:
        con, cliente = s.accept()
        cli = Clientes(con,cliente,True)
        ListaDeClientes(cli)
        n+=1
        _thread.start_new_thread(conexao, tuple([con, cliente, qnt_clientes]))
    elif n==qnt_clientes:
        imprimirListaCliente()
        n+=1
s.close()