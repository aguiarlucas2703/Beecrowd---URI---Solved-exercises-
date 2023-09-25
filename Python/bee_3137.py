def digitos(n):
    return len(str(n))

p = int(input())
t = 0
for i in range(1, p+1):
    t += digitos(i)
print(t)
