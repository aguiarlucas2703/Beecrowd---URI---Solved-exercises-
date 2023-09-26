def cifra(codificado, deslocamento):
    texto_decodificado = ""
    for letra in codificado:
        if letra == ' ':
            texto_decodificado += ' '
        else:
            letra_decodificada = chr(((ord(letra) - ord('A') - deslocamento) % 26) + ord('A'))
            texto_decodificado += letra_decodificada

    return texto_decodificado


N = int(input())

for _ in range(N):
    codificado = input().strip()
    deslocamento = int(input())
    decodificado = cifra(codificado, deslocamento)
    print(decodificado)
