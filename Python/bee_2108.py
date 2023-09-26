g = 0
while True:
    palavra = input().split()
    s = []
    if palavra == ['0']:
        break
    for i in palavra:
        s.append(str(len(i)))
        if len(i) >= g:
            g = len(i)
            aux = i
    a = '-'.join(s)
    print(a)
print()
print(f'The biggest word: {aux}')

