a, b = map(int, input().split())

somab = (b * (b + 1)) // 2

somamin = ((a - 1) * a) // 2 if a > 1 else 0


resultado = somab - somamin
print(resultado)
