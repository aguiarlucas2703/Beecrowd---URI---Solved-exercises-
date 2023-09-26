hi, hf = map(int, input().split())

if hi < hf:
    t = hf - hi
else:
    t = (24 - hi) + hf

print(f'O JOGO DUROU {t} HORA(S)')