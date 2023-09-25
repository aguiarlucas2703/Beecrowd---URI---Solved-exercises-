n = []
x = float(input())
for i in range (100):
    n.append(x)
    print(f'N[{i}] = {x:.4f}')
    if x > 0:
        x = x / 2
