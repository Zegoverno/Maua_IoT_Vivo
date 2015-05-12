import math

def lerPonto():
    return input("digite um ponto no formato (x,y): ").split(',')


def dist(p1,  p2):
    return math.sqrt((float(p1[0]) - float(p2[0])) ** 2 + (float(p1[1]) - float(p2[1])) ** 2)

def angulo(p1, p2):
    return 180*(math.atan2(float(p2[1])-float(p1[1]), float(p2[0])-float(p1[0])))/math.pi

p1 = lerPonto()
p2 = lerPonto()
print ('{0} / {1}º'.format(dist(p1, p2), angulo(p1, p2)))

# Nota: 1.0
# Excelente!!! Dica: O método `math.degrees` converter radianos para graus.
