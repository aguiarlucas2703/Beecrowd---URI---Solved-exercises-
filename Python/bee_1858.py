n = int(input())
t = list(map(int, input().split()))
menor = t.index(min(t))
pessoa = menor + 1
print(pessoa)