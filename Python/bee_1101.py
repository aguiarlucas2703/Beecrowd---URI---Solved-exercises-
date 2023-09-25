while True:
    m, n = map(int, input(). split())
    if m <= 0 or n <= 0:
        break
    if m > n:
        texto = ""
        soma = 0
        for i in range (n, m + 1):
            soma += i
            texto += str(i) + " "
        print(f'{texto}Sum={soma}')
    elif m < n:
        texto = ""
        soma = 0
        for i in range (m, n + 1):
            soma += i
            texto += str(i) + " "
        print(f'{texto}Sum={soma}')