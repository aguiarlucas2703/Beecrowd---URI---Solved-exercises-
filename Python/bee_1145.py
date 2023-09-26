col, cont = map(int, input().split())

linha = 0

for i in range(cont):
    linha += 1
    if linha == col:
        print(i + 1)
        linha = 0
    else:
        print(i + 1, end=' ')
