# Eu fiz esse mas não passou
n1, n2, n3, n4 = [float(x) for x in input().strip().split()]

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media > 5 and media < 7:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media_final = (exame + media) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
else:
    print('Aluno reprovado.')


''' o que estava na internet e passou 

nota = [float(x) for x in input().strip().split(' ')]

media = (2 * nota[0] + 3 * nota[1] + 4 * nota[2] + 1 * nota[3])/10

print(f"Media: {media:.1f}")

if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    exame = float(input().strip())
    print(f"Nota do exame: {exame:.1f}")

    media = (media + exame)/2

    if(media >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media:.1f}")

'''    