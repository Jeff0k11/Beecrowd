N = int(input())
hora = N // 3600
segundos_restantes = N % 3600
minuto = segundos_restantes // 60
segundo = segundos_restantes % 60

print(f'{hora}:{minuto}:{segundo}')