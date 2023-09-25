a, b, c, d = map(int, input().split())
va = 0
if b > c and d > a and c + d > a + b:
    va = 1
if c > 0 and d > 0 and a % 2 == 0:
    va = va + 1
if va == 2:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
