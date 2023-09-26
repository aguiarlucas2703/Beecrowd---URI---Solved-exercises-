def funcoes(x, y):
    r = (3 * x) ** 2 + y ** 2
    b = 2 * (x ** 2) + (5 * y) ** 2
    c = -100 * x + y ** 3
    return r, b, c

def determinar_vencedor(x, y):
    r, b, c = funcoes(x, y)
    if r > b and r > c:
        return 'Rafael ganhou'
    elif b > r and b > c:
        return 'Beto ganhou'
    else:
        return 'Carlos ganhou'

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    resultado = determinar_vencedor(x, y)
    print(resultado)
