inter = 0
gremio = 0
grenal = 0
empate = 0
while True:
    i = 0
    while i < 1:
        a, b = map(int, input().split())
        grenal += 1
        if a > b:
            inter += 1
            i += 1
        elif a < b:
            gremio += 1
            i += 1
        elif a == b:
            empate += 1
            i += 1
    x = 0
    while True:
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())
        if x == 1 or x == 2:
            break
    if x == 2:
        break
if inter > gremio:
    vencedor = 'Inter'
elif inter < gremio:
    vencedor = 'Gremio'
elif inter == gremio:
    vencedor = 'Nao houve vencedor'
print(f'{grenal} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
print(f'{vencedor} venceu')