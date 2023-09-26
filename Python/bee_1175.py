n = [0] * 20

for i in range(20):
    n[i] = int(input())
for i in range(10):
    aux = n[i]
    n[i] = n[19 - i]
    n[19 - i] = aux
for i in range(20):
    print(f'N[{i}] = {n[i]}')

