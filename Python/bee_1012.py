valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

atr = (a * c) / 2

ac = 3.14159 * c ** 2

at = ((a + b) * c) / 2

aq = b ** 2

ar = a * b

print(f'TRIANGULO: {atr:.3f}\nCIRCULO: {ac:.3f}\nTRAPEZIO: {at:.3f}')
print(f'QUADRADO: {aq:.3f}\nRETANGULO: {ar:.3f}')
