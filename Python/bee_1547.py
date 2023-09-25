n = int(input())
for i in range(n):
    QT, S = input().split()
    QT = int(QT)
    S = int(S)
    alunos = input().split()
    alns = []
    for i in alunos:
        alns.append(int(i))
    posicao = 1
    menordif = alns[0] - S
    if menordif < 0:
        menordif = menordif * -1
    for j in range(1, QT):
        diferenca = alns[j] - S
        if diferenca < 0:
            diferenca = -diferenca
        if diferenca < menordif:
             menordif = diferenca
             posicao = j + 1
    print(posicao)

