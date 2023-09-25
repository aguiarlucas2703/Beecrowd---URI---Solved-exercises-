from math import sqrt as raiz
a, b, c = map(float, input().split())
delta = (b ** 2) - (4 * a * c)
if a == 0:
    print('Impossivel calcular')
elif delta >= 0:
    r1 = ((b * (-1)) + raiz(delta)) / (2 * a)
    r2 = ((b * (-1)) - raiz(delta)) / (2 * a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
else:
    print('Impossivel calcular')

