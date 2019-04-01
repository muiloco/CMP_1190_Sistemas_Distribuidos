import socket
import hashlib

HOST = ''
PORT = 5000
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
origem = (HOST, PORT)
udp.bind(origem)

#-----Input de config de numero de maquinas------
qnt_clientes = input("Insira a quantidade de clintes a serem usado:\n")
qnt_clientes = int(qnt_clientes)
qnt_senha = 10**8
qnt_senha = int(qnt_senha / qnt_clientes)
udp.listen(qnt_clientes)

#-----Input de senha desejada-----------
senha = input("Insira sua senha de 8 caracteres:\n")
senha = hashlib.md5(senha.encode()).hexdigest()

#------Procurar por consexoes-----------
flag = True
while flag:
    client = udp.recvfrom()
