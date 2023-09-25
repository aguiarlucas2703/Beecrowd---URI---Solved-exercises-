n, l, d = map(int, input().split())
lc = l * 1000  # Convertendo litros para mililitros
while lc < n * d:
    lc += l * 1000  # Adicionando mais L litros de café em mililitros
lc = lc // 1000  # Convertendo de mililitros de volta para litros
print(lc)