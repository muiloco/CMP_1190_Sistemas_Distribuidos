import itertools
chrs = '0123456789'
n = 8
wl = open('wordlistteste.txt','w') 
count = 10**8
count = count/100
x = 0
for xs in itertools.product(chrs, repeat=n):
    if (x == count):
        break;
    senha = ''.join(xs)
    print (senha)
    wl.write(senha + '\n')
    x = x + 1
wl.close()
    