o = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
el = 0
for i in range(12):
    for j in range(12):
        if i > j and i > 12 - j - 1:
            soma += matriz[i][j]
            el += 1
media = soma / el
if o == 'S':
    print(f'{soma:.1f}')
if o == 'M':
    print(f'{media:.1f}')
