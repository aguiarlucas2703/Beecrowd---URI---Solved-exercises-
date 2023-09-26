while True:
    n = int(input())
    if n == 0:
        break
    suspeitos = []
    ent = input().split()
    for i in ent:
        suspeitos.append(int(i))
    mais_suspeito = -1
    for suspeito in suspeitos:
        if suspeito > mais_suspeito:
            mais_suspeito = suspeito
    segundo_mais_suspeito = -1
    for suspeito in suspeitos:
        if suspeito != mais_suspeito and suspeito > segundo_mais_suspeito:
            segundo_mais_suspeito = suspeito
    for i in range(len(suspeitos)):
        if suspeitos[i] == segundo_mais_suspeito:
            assassino = i + 1
            break
    print(assassino)
