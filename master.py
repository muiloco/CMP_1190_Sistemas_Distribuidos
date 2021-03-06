import socket
import hashlib


lista = []

def clienteJaExiste(parametro):
    x = parametro
    for x in lista:
        return False
    return True

def incluirCliente(cliente):
    lista.append(cliente)

HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
origem = (HOST, PORT)
tcp.bind(origem)

#-----Input de config de numero de maquinas------
qnt_clientes = input("Insira a quantidade de clintes a serem usado:\n")
qnt_clientes = int(qnt_clientes)
qnt_senha = 10**8
qnt_senha = int(qnt_senha / qnt_clientes)
n_clients = 0
#-----Input de senha desejada-----------
senha = input("Insira sua senha de 8 caracteres:\n")
senha = hashlib.md5(senha.encode()).hexdigest()

#------Procurar por consexoes-----------
flag = True
while flag:
    con ,client = tcp.accept()
    print(client, "-conectou")
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(client, msg)
        if clienteJaExiste(client):
            incluirCliente(client)
            n_clients+=1
    print ('Finalizando conexao do cliente', client)
    con.close()