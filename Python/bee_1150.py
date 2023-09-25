x = int(input())
z = 0
while z <= x:
    z = int(input())
    if z > x:
        break
soma = x
total = 1
while soma < z:
    soma += x + total
    total += 1
print(total)