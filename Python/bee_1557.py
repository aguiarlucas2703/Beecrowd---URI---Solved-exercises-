while True:
    n = int(input())
    if n == 0:
        break
    matriz = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(2 ** (i + j))
        matriz.append(row)
    max_digits = len(str(matriz[-1][-1]))
    for row in matriz:
        formatted_row = []
        for num in row:
            formatted_row.append(f'{num:>{max_digits}}')
        print(' '.join(formatted_row))
    print()
