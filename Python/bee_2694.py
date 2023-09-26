n = int(input())

for i in range(n):
    cod = input()
    num = []
    numa = ''
    for j in cod:
        if '0' <= j <= '9':
            numa += j
        else:
            if numa:
                num.append(int(numa))
                numa = ''
    if numa:
        num.append(int(numa))
    s = sum(num)
    print(s)
