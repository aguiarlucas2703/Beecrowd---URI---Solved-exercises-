n = int(input())
for i in range(n):
    div = 0
    a, b = map(int, input().split())
    if b == 0:
        print('divisao impossivel')
    else:
        div = a / b
        print(f'{div}')