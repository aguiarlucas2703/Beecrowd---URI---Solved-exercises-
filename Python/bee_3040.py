n = int(input())

for i in range(n):
    x = False
    a, b, c = map(int, input().split())
    if a >= 200 and a <= 300:
        if b >= 50:
            if c >= 150:
                x = True
    if x == True:
        print('Sim')
    else:
        print('Nao')
