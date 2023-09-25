lista = []
for i in range(5):
    x = int(input())
    lista.append(x)
maior = lista[0]
for k in lista:
    if k > maior:
        maior = k
        indice = lista.index(k) + 1
print(f'{maior}\n{indice}')