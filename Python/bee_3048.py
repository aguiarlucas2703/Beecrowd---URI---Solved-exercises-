n = int(input())
cont = 0
x = []
for i in range(n):
    x.append(int(input()))
ig = x[0]
for i in range(n):
    if x[i] != ig:
        ig = x[i]
        cont += 1
print(cont+1)
