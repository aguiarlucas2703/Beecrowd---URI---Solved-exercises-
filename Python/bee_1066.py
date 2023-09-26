contp = 0
conti = 0
contpo = 0
contn = 0

for i in range(5):
    x = int(input())
    if x % 2 == 0:
        contp += 1
    elif x % 2 != 0:
        conti += 1
    if x > 0:
        contpo += 1
    elif x < 0:
        contn += 1

print(f'{contp} valor(es) par(es)\n{conti} valor(es) impar(es)\n{contpo} valor(es) positivo(s)\n{contn} valor(es) negativo(s)')