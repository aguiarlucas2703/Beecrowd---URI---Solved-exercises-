import math
def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return round((math.pow(phi, n) - math.pow(psi, n)) / sqrt_5, 1)


n = int(input())

x = fibonacci(n)
print(x)
