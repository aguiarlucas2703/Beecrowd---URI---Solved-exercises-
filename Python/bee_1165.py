n = int(input())
for i in range(1, n+1):
    x = int(input())
    contp = 0
    for k in range(1, x+1):
        if x % k == 0:
            contp += 1
    if contp == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
