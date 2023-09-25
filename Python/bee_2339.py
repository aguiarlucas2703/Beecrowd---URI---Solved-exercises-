c, p, f = map(int, input().split())
r = c * f
if r <= p:
    print('S')
else:
    print('N')