cardapio = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

total_compra = 0.0

n = int(input())

for i in range(n):
    produto, quantidade = map(int, input().split())
    total_compra += cardapio[produto] * quantidade

print(f'{total_compra:.2f}')
