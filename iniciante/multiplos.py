a, b = [int(x) for x in input().strip().split()]

if a < b:
    a, b = b, a

print(f'Nao sao multiplos' if(a % b) else 'Sao multiplos')
