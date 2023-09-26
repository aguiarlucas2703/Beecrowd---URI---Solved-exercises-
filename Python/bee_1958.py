def entrada():
    x = float(input())
    return x

def impressao(numero):
    cont = 0
    if numero >= 1 and numero < 10:
        print(f'+{numero:.4f}E+00')
    elif numero > 0 and numero < 1:
        while numero < 1:
            cont += 1
            numero *= 10
        if cont < 10:
            print(f'+{numero:.4f}E-0{cont}')
        else:
            print(f'+{numero:.4f}E-{cont}')
    elif numero >= 10:
        while numero >= 10:
            cont += 1
            numero /= 10
        if cont < 10:
            print(f'+{numero:.4f}E+0{cont}')
        else:
            print(f'+{numero:.4f}E+{cont}')
    elif numero < -1 and numero > -10:
        print(f'-{abs(numero):.4f}E+00')
    elif numero < 0 and numero > -1:
        numero = abs(numero)
        while numero < 1:
            cont += 1
            numero *= 10
        if cont < 10:
            print(f'-{numero:.4f}E-0{cont}')
        else:
            print(f'-{numero:.4f}E-{cont}')
    elif numero <= -10:
        numero = abs(numero)
        while numero >= 10:
            cont += 1
            numero /= 10
        if cont < 10:
            print(f'-{numero:.4f}E+0{cont}')
        else:
            print(f'-{numero:.4f}E+{cont}')
    elif numero == 0.0:
        if str(numero)[0] == '-':
            print(f'{numero:.4f}E+00')
        else:
            print(f'+{numero:.4f}E+00')

impressao(entrada())

