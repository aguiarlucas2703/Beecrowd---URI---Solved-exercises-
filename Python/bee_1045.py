a, b, c = map(float, input().split())

i = [a, b, c]
desc = sorted(i, reverse=True)
a, b, c = desc

if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a ** 2 == b ** 2 + c ** 2:
    print('TRIANGULO RETANGULO')
elif a ** 2 > b ** 2 + c ** 2:
    print('TRIANGULO OBTUSANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a == c != b or b == c != a:
        print('TRIANGULO ISOSCELES')
elif a ** 2 < b ** 2 + c ** 2:
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a == c != b or b == c != a:
        print('TRIANGULO ISOSCELES')