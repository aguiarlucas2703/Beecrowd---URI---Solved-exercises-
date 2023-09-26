n = int(input())

v = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
ad = 0
be = 0

for i in range(n):
    cartas = input().split()
    rad = 0
    rbe = 0
    for j in range(3):
        x = v.index(int(cartas[j]))
        y = v.index(int(cartas[j+3]))
        if x >= y:
            rad += 1
        else:
            rbe += 1
    if rad > rbe:
        ad += 1
    else:
        be += 1
print(ad,be)
