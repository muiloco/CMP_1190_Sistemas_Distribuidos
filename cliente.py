import socket
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta escutando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = "teste"
while True:
    udp.sendto (msg.encode('utf-8'),dest)
udp.close()