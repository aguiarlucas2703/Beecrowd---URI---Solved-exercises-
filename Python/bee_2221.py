t = int(input())

for i in range(t):
    b = int(input())
    ai, di, li = map(int, input().split())
    ag, dg, lg = map(int, input().split())
    if li % 2 == 0:
        golped = ((ai + di) / 2) + b
    else:
        golped = ((ai + di) / 2)
    if lg % 2 == 0:
        golpeg = ((ag + dg) / 2) + b
    else:
        golpeg = ((ag + dg) / 2)
    if golped > golpeg:
        print('Dabriel')
    elif golped < golpeg:
        print('Guarte')
    elif golped == golpeg:
        print('Empate')
