# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:30:46 2019

@author: Fernando R
"""

import hashlib
senha = '00000000'
senha2 = '25252121'

senhahash = hashlib.md5(senha.encode()).hexdigest()

wordlist = open('wordlist.txt','r')
achou = 0

for x in wordlist:
    psenha = hashlib.md5(x.encode()).hexdigest()
    if psenha == senhahash:
        print(x)
        achou = 1
        break
wordlist.close()
if achou == 0:
    print('Senha nao encontrada!')
else:
    print('Finalizado')    