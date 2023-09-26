n = int(input())

i = 1
k = 1

for j in range (n*2):
    print(f'{i} {i ** 2 + (j % 2)} {i ** 3 + (j % 2)}')
    i += (j % 2)