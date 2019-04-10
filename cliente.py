import socket
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta escutando
tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = "teste"
tcp.connect(dest)
while True:
    tcp.send(msg.encode('utf-8'),dest)
tcp.close()