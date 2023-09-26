qtd_casos = int(input())

for _ in range(qtd_casos):
    palavras = input().split(" ")
    palavra1, palavra2 = palavras
    nova_palavra = ''
    if len(palavra1) <= len(palavra2):
        for i in range(len(palavra1)):
            nova_palavra += palavra1[i]
            nova_palavra += palavra2[i]
        nova_palavra += palavra2[len(palavra1):]
    else:
        for i in range(len(palavra2)):
            nova_palavra += palavra1[i]
            nova_palavra += palavra2[i]
        nova_palavra += palavra1[len(palavra2):]
    print(nova_palavra)
