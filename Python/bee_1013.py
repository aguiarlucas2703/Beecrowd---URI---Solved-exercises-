a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

mab = (a + b + abs(a - b))/2

mac = (mab + c + abs(mab - c))/2

mac = int(mac)

print(f'{mac} eh o maior')
