n = int(input())
v = [0] * 10
for i in range(10):
    v[i] = n
    n *= 2
    print(f'N[{i}] = {v[i]}')