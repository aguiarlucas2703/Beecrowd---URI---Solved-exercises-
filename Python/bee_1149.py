val = input().split()
a = int(val[0])
ult = len(val) - 1
n = int(val[ult])
soma = 0
for i in range(n):
    soma += a + i
print(soma)
