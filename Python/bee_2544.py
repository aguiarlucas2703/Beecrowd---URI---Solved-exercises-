import math
while True:
    try:
        cont = 0
        n = int(input())
        r = math.log(n, 2)
        print(f'{r:.0f}')
    except EOFError:
        break