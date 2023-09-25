c = int(input())
for i in range(c):
    texto = input()
    n = 0.00
    for j in range(len(texto)):
        n += 0.01
    print(f'{n:.2f}')