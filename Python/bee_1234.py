while True:
    try:
        sentenca = input()
        nova_sentenca = ""
        maiuscula = True
        for char in sentenca:
            if char.isalpha():
                if maiuscula:
                    nova_sentenca += char.upper()
                else:
                    nova_sentenca += char.lower()
                maiuscula = not maiuscula
            else:
                nova_sentenca += char
        print(nova_sentenca)
    except EOFError:
        break
