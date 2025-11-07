media_litros = 12
horas = int(input())
km = int(input())
litros_na_viagem = (km / media_litros) * horas

print(f'{litros_na_viagem:.3f}')