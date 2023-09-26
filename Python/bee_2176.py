number = list(input())

x = number.count('1')

if x % 2 == 0:
    number.append('0')
else:
    number.append('1')
print(''.join(number))
