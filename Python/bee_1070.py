x = int(input())
i = x
cont = 0
while i >= x:
    if i % 2 != 0:
        cont += 1
        print(f'{i}')
    i += 1
    if cont == 6:
        break