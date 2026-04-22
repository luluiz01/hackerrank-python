entrada = int(input())

horas = entrada // 3600
resto = entrada % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas} horas {minutos} minutos e {segundos} segundos.")
