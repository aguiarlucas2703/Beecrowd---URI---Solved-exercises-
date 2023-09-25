tamanho = int(input())
notas = input().split()
notas1 = []
frequencia = [0] * 101
maior = 0
for i in range(tamanho):
    notas1.append(int(notas[i]))
    frequencia[notas1[i]] += 1
maior = -1
resultado = 0
for j in range(101):
    if frequencia[j] >= maior:
        maior = frequencia[j]
        resultado = j
print(resultado)