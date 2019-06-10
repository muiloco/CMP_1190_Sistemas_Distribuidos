import itertools
chrs = '0123456789'
n = 8
wl = open('wordlistteste.txt','w') 
count = 997
x = 987
count = int(count)
for x in itertools.product(chrs, repeat=n):
    if (x == count):
        break
    senha = ''.join(x)
    print(senha)
    wl.write(senha + '\n')
    x =+ 1
wl.close()