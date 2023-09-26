n = int(input())

c = list('Ho ') * n
c.pop(-1)
c.append('!')
c1 = ''.join(c)

print(c1)
