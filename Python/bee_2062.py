n = int(input())
palavra = input()
palavras = palavra.split()
for i in range(n):
    if len(palavras[i]) == 3:
        if (palavras[i][0] == 'U' and palavras[i][1] == 'R') or (palavras[i][0] == 'O' and palavras[i][1] == 'B'):
            palavras[i] = palavras[i][:2] + 'I'
print(" ".join(palavras))
