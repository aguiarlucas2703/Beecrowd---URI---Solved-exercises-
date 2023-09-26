n = int(input())

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
nu = rdd // 1

print(f'{n}')
print(f'{nc} nota(s) de R$ 100,00')
print(f'{ncq} nota(s) de R$ 50,00')
print(f'{nv} nota(s) de R$ 20,00')
print(f'{nd} nota(s) de R$ 10,00')
print(f'{ndc} nota(s) de R$ 5,00')
print(f'{ndd} nota(s) de R$ 2,00')
print(f'{nu} nota(s) de R$ 1,00')
