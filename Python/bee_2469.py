n = int(input())
notas = input().split()
notas1 = []
frequencia = [0] * 101
for i in range(n):
    notas1.append(int(notas[i]))
    frequencia[notas1[i]] += 1
maior = -1
resultado = 0
for k in range(101):
    if frequencia[k] >= maior:
        maior = frequencia[k]
        resultado = k
print(resultado)
