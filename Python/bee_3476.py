def calculate_harmonic_mean(S, B, C):
    harmonic_mean = 3 / ((1/S) + (1/B) + (1/C))
    return harmonic_mean

S, B, C = map(int, input().split())
previsao_tempo_obra = calculate_harmonic_mean(S, B, C)
print(f'{previsao_tempo_obra:.3f}')
