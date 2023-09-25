letra = input()
frase = input().split()
t = len(frase)
cont = 0
for i in frase:
    if letra in i:
        cont += 1
resultado = (cont/t) * 100
print(f'{resultado:.1f}')
