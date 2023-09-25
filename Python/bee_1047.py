hi, mi, hf, mf = map(int, input().split())
if (hf > hi) and (mf > mi):
    th = hf - hi
    tm = mf - mi
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf > hi and mi > mf:
    th = (hf - hi) - 1
    tm = (mf - mi) + 60
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf == hi and mi > mf:
    th = 23
    tm = (mf - mi) + 60
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf == hi and mf > mi:
    th = 0
    tm = mf - mi
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf > hi and mf == mi:
    th = hf - hi
    tm = 0
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf < hi and mf == mi:
    th = (hf - hi) + 24
    tm = 0
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif hf < hi and mf > mi:
    th = (hf - hi) + 24
    tm = mf - mi
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTOS(S)')
elif hi > hf and mi > mf:
    th = (hf - hi) + 23
    tm = (mf - mi) + 60
    print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
else:
    print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
