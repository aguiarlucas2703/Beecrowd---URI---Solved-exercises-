dia_inicial = int(input().split()[1])
hora = input().split(":")

horai = int(hora[0])
mini = int(hora[1])
segi = int(hora[2])

dia_final = int(input().split()[1])
hora = input().split(":")

horaf = int(hora[0])
minf = int(hora[1])
segf = int(hora[2])

tempoi = segi + mini * 60 + horai * 60 * 60 + dia_inicial * 24 * 60 * 60
tempof = segf + minf * 60 + horaf * 60 * 60 + dia_final * 24 * 60 * 60
dif = tempof - tempoi
d = dif // (24 * 60 * 60)
dif = dif % (24 * 60 * 60)
h = dif // (60 * 60)
dif = dif % (60 * 60)
m = dif // 60
dif = dif % 60
s = dif

print(f'{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)')
