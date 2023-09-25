F1, F2 = map(float, input().split())
flutuacao_total = ((1 + F1 / 100) * (1 + F2 / 100) - 1) * 100
print(f'{flutuacao_total:.6f}')
