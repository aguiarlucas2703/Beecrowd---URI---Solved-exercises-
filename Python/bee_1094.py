n = int(input())

tc = 0
ts = 0
tr = 0
cont = 0
total = 0

for i in range(n):
    x = input().split()
    q = int(x[0])
    t = str(x[1])
    total = total + q
    if t == 'C':
        tc = tc + q
    elif t == 'R':
        tr = tr + q
    elif t == 'S':
        ts = ts + q
    pc = (tc * 100) / total
    pr = (tr * 100) / total
    ps = (ts * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {tc}')
print(f'Total de ratos: {tr}')
print(f'Total de sapos: {ts}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')

