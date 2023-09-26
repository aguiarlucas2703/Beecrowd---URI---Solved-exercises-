n = int(input())

itens = {}

for i in range(n):
    s = 0
    x = int(input())
    for j in range(x):
        item, pre = input().split()
        itens[item] = float(pre)
    p = int(input())
    for j in range(p):
        it, un = input().split()
        un = int(un)
        s += itens[it] * un
    print(f'R$ {s:.2f}')
