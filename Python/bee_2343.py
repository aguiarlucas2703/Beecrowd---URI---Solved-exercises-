n = int(input())

r = []

for a in range(n):
   l = list(map(int, input().split()))
   r.append(l)

r.sort()
igual = 0
raio = 0

for i in range(n):
   if r[i] == igual:
      raio = 1
   else:
      igual = r[i]

print(raio)
