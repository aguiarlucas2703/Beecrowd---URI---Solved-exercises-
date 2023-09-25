while True:
    d, n = input().split()
    if d == '0' and n == '0':
        break
    novo = ''
    for i in n:
        if i != d:
            novo += i
    if novo == '':
        print(0)
    else:
        print(int(novo))
