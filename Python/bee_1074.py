n = int(input())

for i in range(0, n):
    x = int(input())
    if x % 2 == 0:
        if x > 0:
            print('EVEN POSITIVE')
        elif x < 0:
            print('EVEN NEGATIVE')
        elif x == 0:
            print('NULL')
    elif x % 2 != 0:
        if x >= 0:
            print('ODD POSITIVE')
        elif x < 0:
            print('ODD NEGATIVE')
        elif x == 0:
            print('NULL')
