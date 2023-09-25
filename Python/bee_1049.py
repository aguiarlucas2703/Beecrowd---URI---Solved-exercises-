h1 = input()
h2 = input()
h3 = input()
if h1 == 'vertebrado':
    if h2 == 'ave':
        if h3 == 'carnivoro':
            print('aguia')
        elif h3 == 'onivoro':
            print('pomba')
    elif h2 == 'mamifero':
        if h3 == 'onivoro':
            print('homem')
        elif h3 == 'herbivoro':
            print('vaca')
elif h1 == 'invertebrado':
    if h2 == 'inseto':
        if h3 == 'hematofago':
            print('pulga')
        elif h3 == 'herbivoro':
            print('lagarta')
    elif h2 == 'anelideo':
        if h3 == 'hematofago':
            print('sanguessuga')
        elif h3 == 'onivoro':
            print('minhoca')
