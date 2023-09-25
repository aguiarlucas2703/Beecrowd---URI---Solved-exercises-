t = int(input())
p = 0
v = [0] * 1000
while p < 1000:
    for i in range(0, t):
        print(f'N[{p}] = {i}')
        p += 1
        if p >= 1000:
            break
