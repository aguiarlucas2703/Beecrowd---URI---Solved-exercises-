m = []

op = input()

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    m.append(linha)

soma = 0.0

for i in range(12):
    for j in range(12):
        if i > j:
           soma += m[i][j]

media = soma / 66

if op == 'S':
    print(f'{soma:.1f}')
if op == 'M':
    print(f'{media:.1f}')
