peca1 = input().split()

cod1 = int(peca1[0])
num1 = int(peca1[1])
val1 = float(peca1[2])

peca2 = input().split()

cod2 = int(peca2[0])
num2 = int(peca2[1])
val2 = float(peca2[2])

total = num1 * val1 + num2 * val2

print(f'VALOR A PAGAR: R$ {total:.2f}')
