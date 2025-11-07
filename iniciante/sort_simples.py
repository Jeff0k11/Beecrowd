valores_originais = list(map(int, input().strip().split()))

valores_ordenados = sorted(valores_originais)
for valor in valores_ordenados:
    print(valor)
print()
for valor in valores_originais:
    print(valor)