while True:
    lista = []
    while len(lista) < 2:
        x = float(input())
        if 0 <= x <= 10:
            lista.append(x)
        else:
            print('nota invalida')
    media = sum(lista) / 2
    print(f'media = {media:.2f}')
    y = 0
    while True:
        print('novo calculo (1-sim 2-nao)')
        y = int(input())
        if y == 1 or y == 2:
            break
    if y == 2:
        break
