n = int(input())
for i in range(n):
    a = set(input().split())
    b = list(a)
    b.sort()
    for j in range(len(b)):
        if j == len(b) - 1:
            print(b[j])
        else:
            print(b[j], end =' ')