codigo, quantidade = [int(x) for x in input().strip().split(' ')]
preco = [4.00, 4.50, 5.00, 6.00, 10.00]

total = quantidade * preco[codigo - 1]

print(f'Total: R$ {total:.2f}')