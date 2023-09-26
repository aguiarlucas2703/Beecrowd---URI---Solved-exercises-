n = int(input())

bran = 0
pret = 0

if (n*n) % 2 == 0:
    pret = (n*n) / 2
    bran = (n*n) / 2
else:
    bran = ((n * n) // 2) + 1
    pret = (n*n) // 2

bran = int(bran)
pret = int(pret)
print(f'{bran:} casas brancas e {pret} casas pretas')

