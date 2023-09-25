n = int(input())
for i in range(n):
    nome, esc, nome2, esc2 = input().split()
    x, y = map(int, input().split())
    z = x + y
    if z % 2 == 0:
        if esc == 'PAR':
            print(nome)
        else:
            print(nome2)
    else:
        if esc == 'IMPAR':
            print(nome)
        else:
            print(nome2)

