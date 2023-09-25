c = int(input())
op = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
for i in range(12):
    soma += matriz[i][c]
media = soma / 12
if op == 'S':
    print(f'{soma:.1f}')
elif op == 'M':
    print(f'{media:.1f}')