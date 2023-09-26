turma = 1

while True:
    n = int(input())
    if n == 0:
        break
    alunos = []
    maior = 0
    for i in range(n):
        codigo, nota = map(int, input().split())
        if nota > maior:
            alunos = [codigo]
            maior = nota
        elif nota == maior:
            alunos.append(codigo)
    print(f'Turma {turma}')
    print(f' '.join(str(codigo) for codigo in alunos),'')
    print('')
    turma += 1
