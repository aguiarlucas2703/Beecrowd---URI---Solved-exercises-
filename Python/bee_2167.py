n = int(input())
x = list(map(int, input().split()))

queda = 0

for i in range(1, n):
    if x[i] < x[i-1]:
        queda = i + 1
        break

print(f'{queda}')