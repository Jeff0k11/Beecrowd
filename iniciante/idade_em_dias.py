idade_em_dias = int(input())

if idade_em_dias >= 365:
    print(f'{idade_em_dias//365} ano(s)')
    idade_em_dias = idade_em_dias % 365
else:
    print('0 ano(s)')

if idade_em_dias >=30:
    print(f'{idade_em_dias//30} mes(es)')
    idade_em_dias = idade_em_dias % 30

print(f'{idade_em_dias} dia(s)')