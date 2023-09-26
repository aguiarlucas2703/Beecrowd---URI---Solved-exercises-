s = 0
a = 1
b = 1

for a in range(1, 39, 2):
    c = a / b
    s += c
    b *= 2

print(f'{s:.2f}')