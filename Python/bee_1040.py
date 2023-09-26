n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    ex = float(input())
    print(f'Nota do exame: {ex:.1f}')
    mediaf = (media + ex) / 2
    if mediaf >= 5.0:
        print(f'Aluno aprovado.\nMedia final: {mediaf:.1f}')
    else:
        print(f'Aluno reprovado.\nMedia final: {mediaf:.1f}')