n = int(input())

for i in range(n):
    cod = input()
    resultado = []
    m = len(cod) // 2
    for j in range(m - 1, -1, -1):
        resultado.append(cod[j])
    for j in range(len(cod) - 1, m - 1, -1):
        resultado.append(cod[j])
    print(''.join(resultado))
