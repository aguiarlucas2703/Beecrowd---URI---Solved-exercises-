t = int(input())
competidores = list(map(int, input().split()))

cont = 0

for i in range(5):
    if competidores[i] == t:
        cont += 1

print(cont)
