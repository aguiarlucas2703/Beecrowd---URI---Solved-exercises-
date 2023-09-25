x = [None] * 10
for i in range(len(x)):
    x[i] = int(input())
for i in range(len(x)):
    if x[i] <= 0:
        x[i] = 1
    print(f'X[{i}] = {x[i]}')