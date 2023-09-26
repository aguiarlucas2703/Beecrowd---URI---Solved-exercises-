n, c, m = map(int, input().split())
C = list(map(int, input().split()))
F = list(map(int, input().split()))

a = 0

for i in C:
    if i not in F:
        a += 1

print(a)
