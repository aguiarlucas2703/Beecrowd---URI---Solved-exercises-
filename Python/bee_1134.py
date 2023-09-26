alcool = 0
gal = 0
diesel = 0

while True:
    x = int(input())
    if x < 1 or x > 4:
        continue
    if x == 1:
        alcool += 1
    elif x == 2:
        gal += 1
    elif x == 3:
        diesel += 1
    elif x == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gal}')
print(f'Diesel: {diesel}')
