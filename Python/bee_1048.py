salario = float(input())
if salario <= 400.00:
    salarioa = (salario * 0.15) + salario
    print(f'Novo salario: {salarioa:.2f}\nReajuste ganho: {salario * 0.15:.2f}')
    print(f'Em percentual: 15 %')
elif 400.01 <= salario <= 800.00:
    salarioa = (salario * 0.12)
    print(f'Novo salario: {salarioa:.2f}\nReajuste ganho: {salario * 0.12:.2f}')
    print(f'Em percentual: 12 %')
elif 800.01 <= salario <= 1200.00:
    salarioa = (salario * 0.10) + salario
    print(f'Novo salario: {salarioa:.2f}\nReajuste ganho: {salario * 0.10:.2f}')
    print(f'Em percentual: 10 %')
elif 1200.01 <= salario <= 2000.00:
    salarioa = (salario * 0.07) + salario
    print(f'Novo salario: {salarioa:.2f}\nReajuste ganho: {salario * 0.07:.2f}')
    print(f'Em percentual: 7 %')
else:
    salarioa = (salario * 0.04) + salario
    print(f'Novo salario: {salarioa:.2f}\nReajuste ganho: {salario * 0.04:.2f}')
    print(f'Em percentual: 4 %')