def bin(n):
    cont = 0
    while n > 0:
        cont += n % 2
        n //= 2
    return(cont)


m = int(input())

for i in range(m):
    k = int(input())
    res = bin(k)
    print(res)
