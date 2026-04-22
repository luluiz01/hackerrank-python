tempo_gasto = int(input())
media_em_KM = int(input())

distancia = tempo_gasto * media_em_KM
litros = distancia / 12

print(f"{litros:.3f}")
