reais, centavos = [int(x) for x in input().strip().split('.')]
reais = reais * 100 + centavos
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print('NOTAS:')
for nota in notas:
    quantidade = reais // nota   
    print(f'{quantidade} nota(s) de R$ {(nota/100):.2f}')
    reais %= nota

print('MOEDAS:')
for moeda in moedas:
    quantidade = reais // moeda
    print(f'{quantidade} moeda(s) de R$ {(moeda/100):.2f}')
    reais %= moeda



