num_casos = int(input())
for _ in range(num_casos):
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