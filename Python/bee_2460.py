n = int(input())
p = list(map(int, input().split()))
n2 = int(input())
p2 = list(map(int, input().split()))

for i in p2:
    p.remove(i)

print(' '.join(map(str,p)))
