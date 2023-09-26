c, q = map(int, input().split())

lanches = [0.0, 4.0, 4.5, 5.0, 2.0, 1.5]
t = lanches[c] * q

print(f'Total: R$ {t:.2f}')