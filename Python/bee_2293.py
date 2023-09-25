n, m = map(int, input().split())
campo = []
campo2 = []
for _ in range(n):
    linhas = input().split()
    linhas_int = []
    for k in linhas:
        linhas_int.append(int(k))
    campo.append(linhas_int)
max_colheita = 0
for i in range(n):
    linha = 0
    for j in range(m):
        linha += campo[i][j]
    if linha > max_colheita:
        max_colheita = linha
for i in range(m):
    coluna = 0
    for j in range(n):
        coluna += campo[j][i]
    if coluna > max_colheita:
        max_colheita = coluna
print(max_colheita)

