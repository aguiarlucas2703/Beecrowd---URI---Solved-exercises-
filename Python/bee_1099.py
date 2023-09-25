n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        imp = 0
        for j in range(b + 1, a):
            if j % 2 != 0:
                imp += j
        print(f'{imp}')
    elif a < b:
        imp = 0
        for j in range(a + 1, b):
            if j % 2 != 0:
                imp += j
        print(f'{imp}')
    elif a == b:
        imp = 0
        print(f'{imp}')