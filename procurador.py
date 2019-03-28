# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:30:46 2019

@author: Fernando R
"""

import hashlib
senha = '00000064'
senhahash = hashlib.md5(senha.encode()).hexdigest()

wordlist = open('wordlist.txt','r')
achou = 0

for x in wordlist:
    psenha = x[:8]
    psenha = hashlib.md5(psenha.encode()).hexdigest()
    if psenha == senhahash:
        print('Sua senha babaca:')
        print(x)
        achou = 1
        break
wordlist.close()
if achou == 0:
    print('Senha nao encontrada!')
else:
    print('Finalizado')