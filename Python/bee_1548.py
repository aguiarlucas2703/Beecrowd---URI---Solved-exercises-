n = int(input())

for i in range(n):
    x = int(input())
    val = list(map(int, input().split()))
    val2 = val.copy()
    val2.sort(reverse=True)
    cont = 0
    for j in range(len(val)):
        if val[j] == val2[j]:
            cont += 1
    print(cont)
