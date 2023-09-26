p = input().split()

msg = ''

for i in p:
    for l in range(1, len(i), 2):
        msg += i[l]
    msg += ' '

print(msg[:-1])

