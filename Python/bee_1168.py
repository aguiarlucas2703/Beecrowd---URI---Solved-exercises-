n = int(input())

for i in range(n):
    num = list(input())
    tam = len(num)
    led = 0
    for j in range(tam):
        if num[j] == '1':
            led += 2
        if num[j] == '2':
            led += 5
        if num[j] == '3':
            led += 5
        if num[j] == '4':
            led += 4
        if num[j] == '5':
            led += 5
        if num[j] == '6':
            led += 6
        if num[j] == '7':
            led += 3
        if num[j] == '8':
            led += 7
        if num[j] == '9':
            led += 6
        if num[j] == '0':
            led += 6
    print(f'{led} leds')
