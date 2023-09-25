t = int(input())
for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1), float(g2)
    cont = 0
    while pa <= pb:
        pa = int(pa * (g1/100)) + pa
        pb = int(pb * (g2/100)) + pb
        cont += 1
        if cont > 100:
            print('Mais de um seculo.')
            break
    if cont <= 100:
        print(f'{cont} anos.')