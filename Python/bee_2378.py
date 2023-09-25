n, c = input().split()
n, c = int(n), int(c)
soma = 0
for i in range(n):
    s, e = input().split()
    s, e = int(s), int(e)
    soma -= s
    soma += e
    if soma > c:
        break
if soma > c:
    print('S')
else:
    print('N')