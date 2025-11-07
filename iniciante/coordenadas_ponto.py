x, y = [float(x) for x in input().strip().split()]

if (x > 0.0):
    if (y > 0.0):
        print('Q1')
    elif (y < 0.0):
        print('Q4')
    else:
        print('Eixo x')

elif (x < 0.0):
    if (y > 0.0):
        print('Q2')
    elif (y < 0.0):
        print('Q3')
    else:
        print('Eixo x')

else:
    if (y < 0.0):
        print('Eixo y')
    elif(y > 0.0):
        print('Eixo y')
    else:
        print('Origem')