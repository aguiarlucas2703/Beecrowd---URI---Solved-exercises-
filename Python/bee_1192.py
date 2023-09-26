def sol(n):
    di1 = int(n[0])
    alf = n[1]
    di2 = int(n[2])
    if alf.isupper():
        if di1 != di2:
            return di2 - di1
        elif di1 == di2:
            return di1 * di2
        else:
            return 0
    elif alf.islower():
        if di1 != di2:
            return di1 + di2
        elif di1 == di2:
            return di1 * di2
        else:
            return 0

n = int(input())
for i in range(n):
    ent = input()
    r = sol(ent)
    print(r)
