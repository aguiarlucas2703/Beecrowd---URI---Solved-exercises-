t = int(input())
for i in range(1, t+1):
    x = input().split()
    if x[0] == 'pedra':
        if x[1] == 'lagarto' or x[1] == 'tesoura':
            print(f'Caso #{i}: Bazinga!')
        elif x[1] == 'papel' or x[1] == 'Spock':
            print(f'Caso #{i}: Raj trapaceou!')
        elif x[1] == x[0]:
            print(f'Caso #{i}: De novo!')
    elif x[0] == 'papel':
        if x[1] == 'pedra' or x[1] == 'Spock':
            print(f'Caso #{i}: Bazinga!')
        elif x[1] == 'tesoura' or x[1] == 'lagarto':
            print(f'Caso #{i}: Raj trapaceou!')
        elif x[1] == x[0]:
            print(f'Caso #{i}: De novo!')
    elif x[0] == 'tesoura':
        if x[1] == 'papel' or x[1] == 'lagarto':
            print(f'Caso #{i}: Bazinga!')
        elif x[1] == 'Spock' or x[1] == 'pedra':
            print(f'Caso #{i}: Raj trapaceou!')
        elif x[1] == x[0]:
            print(f'Caso #{i}: De novo!')
    elif x[0] == 'lagarto':
        if x[1] == 'Spock' or x[1] == 'papel':
            print(f'Caso #{i}: Bazinga!')
        elif x[1] == 'pedra' or x[1] == 'tesoura':
            print(f'Caso #{i}: Raj trapaceou!')
        elif x[1] == x[0]:
            print(f'Caso #{i}: De novo!')
    elif x[0] == 'Spock':
        if x[1] == 'tesoura' or x[1] == 'pedra':
            print(f'Caso #{i}: Bazinga!')
        elif x[1] == 'lagarto' or x[1] == 'papel':
            print(f'Caso #{i}: Raj trapaceou!')
        elif x[1] == x[0]:
            print(f'Caso #{i}: De novo!')
