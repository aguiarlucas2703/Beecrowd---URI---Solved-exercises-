lista = set()
while True:
        try:
            lista.add(input())
        except EOFError:
            print(len(lista))
            break

