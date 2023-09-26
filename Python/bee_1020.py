id = int(input())

ano = id // 365
r = id % 365
m = r // 30
d = r % 30

print(f'{int(ano)} ano(s)\n{int(m)} mes(es)\n{int(d)} dia(s)')
