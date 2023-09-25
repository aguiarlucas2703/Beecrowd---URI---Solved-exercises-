N = int(input())
n = list(map(int, input().split()))
menor = n[0]
posicao = 0
for i in range(N):
    if n[i] < menor:
        menor = n[i]
        posicao = i
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')

