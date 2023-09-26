par = []
impar = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        ind = 0
        for p in par:
            print(f"par[{ind}] = {p}")
            ind += 1
        par = []
    if len(impar) == 5:
        ind = 0
        for imp in impar:
            print(f"impar[{ind}] = {imp}")
            ind += 1
        impar = []

if len(impar) > 0:
    ind = 0
    for imp in impar:
        print(f"impar[{ind}] = {imp}")
        ind += 1
if len(par) > 0:
    ind = 0
    for p in par:
        print(f"par[{ind}] = {p}")
        ind += 1
