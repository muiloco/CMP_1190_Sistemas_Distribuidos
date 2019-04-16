# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:51:41 2019

@author: Fernando R
"""

import socket
import _thread
import queue
import hashlib

listaDeCliente = []
filaDeServico = queue.LifoQueue(maxsize=1000)

#=================classes===============
class Servico:
    def __init__(self, inicio, fim, status):
        self.inicio = inicio
        self.fim = fim
        self.status = status
    
    def alterarStatus(self, novostatus):
        self.status = novostatus
    
    def retornarRange(self):
        return self.inicio, self.fim

class Clientes:
    cont_cliente=0
    def __init__(self, cliente, ipcliente, status):
        self.cliente = cliente
        self.ipcliente = ipcliente
        self.status = status
    
    def imprimir(self):
        print("Cliente:", self.ipcliente)

#=================Metodos de Gerencia do Server=============

def ListaDeClientes(objCliente):
    listaDeCliente.append(objCliente)

def jaECliente(objCliente):
    if objCliente in listaDeCliente:
        return False
    else: return True

def imprimirListaCliente():
    n = len(listaDeCliente)
    x=0
    while x < n:
        cliente = listaDeCliente[x]
        cliente.imprimir()
        x+=1

def gerarFilaDeServicos(qnt_senha):
    qnt_senhaServico = qnt_senha / 1000
    cont = 0
    inicio = 0
    x = 0
    while x < qnt_senhaServico:
        if cont == qnt_senhaServico - 1:
            fim = cont
            servico = Servico(inicio, fim, 'Aguardando')
            filaDeServico.put(servico)
            inicio = fim + 1
            cont = 0
        cont += 1
        x += 1

def conexao(con, cliente, senha):
    print("Conectado:", cliente)
    servico = filaDeServico.get()
    inicio, fim = servico.retornarRange()
    inicio = str(inicio)
    fim = str(fim)
    dados = senha + ';' + inicio + ';' + fim
    con.send(dados.encode('utf-8'))
    while True:
        resposta = con.recv(1024)
        if not msg: break
        print(msg, cliente)
    print("Finalizado conexao:", cliente)
    con.close()
    _thread.exit()

#===============Servidor Config=====================
server = socket.socket()
host = socket.gethostname()
port = 12345
server.bind((host, port))
server.listen(1)

#=============Parametros do Servidor===========
qnt_clientes = input("Insira a quantidade de clintes a serem usado:\n")
qnt_clientes = int(qnt_clientes)
senha = input("Senha de 8 caracteres:")
senha = hashlib.md5(senha.encode()).hexdigest()
qnt_senha = 10**8

n = 0
msg = "testeteste"
while True:
    con, addr = server.accept()
    cli = Clientes(con,addr,True)
    if jaECliente(cli):
        ListaDeClientes(cli)
        _thread.start_new_thread(conexao, tuple([con, addr, senha]))
server.close()