import itertools
chrs = '0123456789'
n = 8
wl = open('wordlist.txt','w') 
for xs in itertools.product(chrs, repeat=n):
    senha = ''.join(xs)
    print (senha)
    wl.write(senha + '\n')
wl.close()
    
