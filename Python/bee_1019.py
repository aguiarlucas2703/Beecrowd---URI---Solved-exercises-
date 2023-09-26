n = int(input())

h = n / 3600
r = n % 3600
min = r / 60
s = r % 60

print(f'{int(h)}:{int(min)}:{int(s)}')
