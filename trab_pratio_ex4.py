def ler():
    lados =[]
    for i in range(3):
        if i != 2:
            lados.append(int(input("digite um cateto:")))
        else:
            lados.append(int(input("digite a hipotenusa")))
    return lados


def triangulo(lados):
    if lados[2]**2 == lados[1]**2 + lados[0]**2:
        return lados[0]*lados[1]/2
    else:
        return 0

lados = ler()
if triangulo(lados) > 0:
    print('os lados formam um triangulo retangul e sua area e: {0}'.format(triangulo(lados)))
else:
    print('os lados {0}, {1} e {2} nao formam um triangulo'.format(lados[0],  lados[1],  lados[2]))

# Nota: 1.0
# Ótimo!!!
