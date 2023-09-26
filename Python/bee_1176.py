t = int(input())

for i in range(t):
    x = int(input())
    a = 0
    b = 1
    fib = []
    for j in range(x+1):
        fib.append(a)
        c = a + b
        a = b
        b = c
    print(f'Fib({x}) = {fib[-1]}')
