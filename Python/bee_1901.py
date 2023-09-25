n = int(input())
floresta = []
for i in range(n):
    linha = list(map(int, input().split()))
    floresta.append(linha)
pos = []
for i in range(2*n):
    posicao = list(map(int, input().split()))
    pos.append(posicao)
cont = []
for posicao in pos:
    x, y = posicao
    esp = floresta[x-1][y-1]
    if esp not in cont:
        cont.append(esp)
print(len(cont))
