while True:
    try:
        texto = input().split('-')
        cobol = ''
        for palavra in texto:
            x = palavra[0].lower()
            y = palavra[len(palavra) - 1].lower()
            if len(cobol) == 0 and (x == 'c' or y == 'c'):
                cobol += 'c'
            elif len(cobol) == 1 and (x == 'o' or y == 'o'):
                cobol += 'o'
            elif len(cobol) == 2 and (x == 'b' or y == 'b'):
                cobol += 'b'
            elif len(cobol) == 3 and (x == 'o' or y == 'o'):
                cobol += 'o'
            elif len(cobol) == 4 and (x == 'l' or y == 'l'):
                cobol += 'l'

        if cobol == 'cobol':
            print('GRACE HOPPER')
        else:
            print('BUG')
    except EOFError:
        break