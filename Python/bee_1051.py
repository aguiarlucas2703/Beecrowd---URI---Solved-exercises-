renda = float(input())
if 0 <= renda <= 2000:
    print('Isento')
elif 2000 < renda <= 3000:
    rendai = (renda - 2000.0) * 0.08
    print(f'R$ {rendai:.2f}')
elif 3000 < renda <= 4500:
    rendai = (renda - 3000.00) * 0.18 + (1000 * 0.08)
    print(f'R$ {rendai:.2f}')
elif renda > 4500:
    rendai = (renda - 4500.00) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {rendai:.2f}')