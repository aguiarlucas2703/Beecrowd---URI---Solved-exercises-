x = int(input())
y = int(input())
figs = []
num = [0] * (x + 1)
for i in range(y):
    figs.append(int(input()))
result = 0
for figuras in figs:
    num[figuras] = 1
for j in range(1, x + 1):
    if num[j] == 0:
        result += 1
print(result)