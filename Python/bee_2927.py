a, c, x, y = input().split()
a, c, x, y = int(a), int(c), int(x), int(y)
infuncional = x + y
funcional = c - infuncional
if a >= funcional:
    if x > y/2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
else:
    print('Igor feliz!')
