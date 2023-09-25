while True:
    try:
        r = 0
        n = int(input())
        l = list(map(int, input().split()))
        r = max(l)
        if r < 10:
            print(1)
        elif 10 <= r < 20:
            print(2)
        elif r >= 20:
            print(3)
    except EOFError:
        break