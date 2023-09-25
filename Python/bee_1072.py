n = int(input())
contpo = 0
contn = 0
for i in range(0, n):
    x = int(input())
    if 10 <= x <= 20:
        contpo += 1
    else:
        contn += 1
print(f'{contpo} in\n{contn} out')