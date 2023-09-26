def calcular_distancia_media():
    soma_distancias = 0
    numero_amigos = 0
    while True:
        try:
            nome_amigo = input()
            distancia = int(input())

            soma_distancias += distancia
            numero_amigos += 1
        except EOFError:
            break
    if numero_amigos > 0:
        distancia_media = soma_distancias / numero_amigos
        return distancia_media
    else:
        return None

dm = calcular_distancia_media()

if dm is not None:
    print(f'{dm:.1f}')
