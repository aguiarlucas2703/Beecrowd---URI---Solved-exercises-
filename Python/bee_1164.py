n = int(input())

for i in range(0, n):
    x = int(input())
    div = 0
    for k in range(1, x):
        if x % k == 0:
            div += k
    if div == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
