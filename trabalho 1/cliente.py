import socket               
import itertools
import hashlib

def gerarWordList(inicio,fim):
    chrs = '0123456789'
    n = 8
    wl = open('wordlistteste.txt','w') 
    count = fim
    x = inicio
    count = int(count)
    for xs in itertools.product(chrs, repeat=n):
        if (x == count):
            break
        senha = ''.join(xs)
        wl.write(senha + '\n')
        x =+ 1
    wl.close()

def buscaSenha(senha):
    wordlist = open('wordlist.txt','r')
    achou = False
    for x in wordlist:
        psenha = x[:8]
        psenha = hashlib.md5(psenha.encode()).hexdigest()
        if psenha == senha:
            senhareal = psenha
            achou = True
            break
    wordlist.close()
    if achou == True:
        return True, senhareal
    else:
        return False

servidor = socket.socket()
host = socket.gethostname()
port = 12345

servidor.connect((host, port))


while True:
    msg = servidor.recv(1024)
    dados = msg.split(';')
    hashsenha = dados[0]
    inicio = int(dados[1])
    fim = int(dados[2])
    gerarWordList(inicio,fim)
    flag, senhareal = buscaSenha(hashsenha)
    if flag:
        resposta = 'Achou;' + senhareal
        servidor.send(resposta.encode('utf-8'))
        break
    else:
        resposta = 'Servico Completo;'
        servidor.send(resposta.encode('utf-8'))
servidor.close()