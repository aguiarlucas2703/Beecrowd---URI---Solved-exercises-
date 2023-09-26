n = float(input())

n = n + 0.001
nc = n // 100
rc = n % 100
ncq = rc // 50
rcq = rc % 50
nv = rcq // 20
rv = rcq % 20
nd = rv // 10
rd = rv % 10
ndc = rd // 5
rdc = rd % 5
ndd = rdc // 2
rdd = rdc % 2
num = rdd // 1
rum = rdd % 1
mdc = rum // 0.50
rmdc = rum % 0.50
mvc = rmdc // 0.25
rmvc = rmdc % 0.25
mdd = rmvc // 0.10
rmdd = rmvc % 0.10
mc = rmdd // 0.05
rmc = rmdd % 0.05
md1 = rmc // 0.01

print(f'NOTAS:')
print(f'{nc:.0f} nota(s) de R$ 100.00')
print(f'{ncq:.0f} nota(s) de R$ 50.00')
print(f'{nv:.0f} nota(s) de R$ 20.00')
print(f'{nd:.0f} nota(s) de R$ 10.00')
print(f'{ndc:.0f} nota(s) de R$ 5.00')
print(f'{ndd:.0f} nota(s) de R$ 2.00')
print(f'MOEDAS:')
print(f'{num:.0f} moeda(s) de R$ 1.00')
print(f'{mdc:.0f} moeda(s) de R$ 0.50')
print(f'{mvc:.0f} moeda(s) de R$ 0.25')
print(f'{mdd:.0f} moeda(s) de R$ 0.10')
print(f'{mc:.0f} moeda(s) de R$ 0.05')
print(f'{md1:.0f} moeda(s) de R$ 0.01')
