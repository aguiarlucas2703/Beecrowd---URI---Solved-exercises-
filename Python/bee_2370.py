N, T = map(int, input().split())

alunos = {}

for i in range(N):
    nome, habilidade = input().split()
    habilidade = int(habilidade)
    alunos[nome] = habilidade

times = []

for i in range(T):
    times.append([])

alunos_ordenados = sorted(alunos.items(), key=lambda x: (-x[1], x[0]))

for i in range(len(alunos_ordenados)):
    aluno, j = alunos_ordenados[i]
    times[i % T].append(aluno)

for i in range(T):
    times[i].sort()

for i in range(len(times)):
    print(f"Time {i + 1}")
    for j in range(len(times[i])):
        print(times[i][j])
    print()
