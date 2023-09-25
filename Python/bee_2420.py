N = int(input())
secoes = list(map(int, input().split()))
soma_esquerda = [0] * (N + 1)
soma_direita = [0] * (N + 1)
for i in range(1, N + 1):
    soma_esquerda[i] = soma_esquerda[i - 1] + secoes[i - 1]
for i in range(N - 1, -1, -1):
    soma_direita[i] = soma_direita[i + 1] + secoes[i]
for i in range(1, N + 1):
    if soma_esquerda[i] == soma_direita[i]:
        print(i)
        break