hi, mi, hf, mf = map(int, input().split())

#calcula o tempo inicial em minutos desde a meia-noite
ti = hi * 60 + mi
#calcula o tempo final em minutos desde a meia-noite
tf = hf * 60 + mf

if ti < tf:
    duracao = tf - ti
elif ti > tf:
    duracao = (24 * 60 - ti) - tf
else:
    duracao = 24 * 60

#converte a duração para horas e minutos
horas = duracao // 60
minutos = duracao % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')