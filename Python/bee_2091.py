while True:
    n = int(input())
    if n == 0:
        break
    num = input().split()
    aux = []
    for i in range(len(num)):
      num[i] = int(num[i])
    for i in num:
       if i in aux:
            aux.remove(i)
       else:
            aux.append(i)
    print(aux[0])
