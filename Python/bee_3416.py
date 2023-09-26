n, l, d = map(int, input().split())

lc = l * 1000

while lc < n * d:
    lc += l * 1000

lc = lc // 1000

print(lc)
