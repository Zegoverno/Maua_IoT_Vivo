def entrada ():
	return int(input("Digite um numero: "))

def par (x):
    if not x % 2 :
        print('O numero {0} é par'.format(x))
    else:
        print('O numero {0} é impar'.format(x))
    
x = entrada()
par(x)
