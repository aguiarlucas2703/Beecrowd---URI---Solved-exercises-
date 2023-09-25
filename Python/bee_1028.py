n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    while b != 0:
        aux = b
        b = a % b
        a = aux
    print(a)