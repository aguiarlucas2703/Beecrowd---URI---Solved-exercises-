while True:
    try:
        string = list(input())
        n = int(input())
        cont = 0
        for i in range(len(string)):
            if string[i] == 'R':
                cont += 1
            elif string[i] == 'W':
                cont += 1
            if string[i] != string[i+1]:
                cont += 1
        print(cont)
    except IndexError:
        pass


    except EOFError:
      break