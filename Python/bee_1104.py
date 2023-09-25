while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    x = set(map(int, input().split()))
    y = set(map(int, input().split()))
    cartasc = x & y
    resultado = min(len(x), len(y)) - len(cartasc)
    print(resultado)