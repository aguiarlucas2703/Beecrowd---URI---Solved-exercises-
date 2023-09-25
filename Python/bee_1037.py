a = float(input())
if 0 <= a <= 25.0000:
    print('Intervalo [0,25]')
elif 25 < a <= 50.0000:
    print('Intervalo (25,50]')
elif 50 < a <= 75.0000:
    print('Intervalo (50,75]')
elif 75 < a <= 100.0000:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

