while True:
    try:
        n = int(input())
        matriz = []
        for i in range(n):
            linha = []
            for j in range(n):
                if i + j == n - 1:
                    linha.append(2)
                elif i == j:
                    linha.append(1)
                else:
                    linha.append(3)
            matriz.append(linha)
        for i in range(n):
            for j in range(n):
                if j == n - 1:
                    print(matriz[i][j])
                else:
                    print(matriz[i][j], end='')
    except EOFError:
        break
