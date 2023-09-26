n, d = map(int, input().split())

menor = d

for i in range(n):
    x = int(input())
    d += x
    menor = min(menor, d)

print(menor)
