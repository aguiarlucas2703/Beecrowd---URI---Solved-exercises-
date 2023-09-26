n = int(input())

for i in range(n):
    a, b = input().split()
    a_len = len(a)
    b_len = len(b)
    if a_len < b_len:
        print("nao encaixa")
    else:
        if a[-b_len:] == b:
            print("encaixa")
        else:
            print("nao encaixa")