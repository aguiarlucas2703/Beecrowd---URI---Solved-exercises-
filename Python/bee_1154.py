soma = 0
cont = 0

while True:
    x = int(input())
    if x < 0:
        break
    soma += x
    cont += 1

media = soma/cont

print(f'{media:.2f}')
