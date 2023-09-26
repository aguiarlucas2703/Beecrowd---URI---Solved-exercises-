i = 0
soma = 0
while i < 2:
    n = float(input())
    if 0 <= n <= 10:
        soma += n
        i += 1
    else:
        print('nota invalida')
media = soma / 2
print(f'media = {media:.2f}')