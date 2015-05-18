import math

def ler():
    return input('digite um ponto no formato cartesiano (x,y,z): ').split(',')

def conv(pto):
    E = 0.00669454185
    A = 6378160
    geo = []
    h = 0
    n =1
    for i in range(5):
        fi = math.atan(float(pto[2])/p(pto)*(E*n/(n+h)))
        n = A/(math.sqrt(1-E*(math.sin(fi))**2))
        h = p(pto)/math.cos(fi)-n
    geo.append(180*math.atan(float(pto[0])/float(pto[1])/math.pi))
    geo.append(180*fi/math.pi)
    geo.append(h)
    return geo

def p(pto):
    return math.sqrt(float(pto[0]) ** 2 + float(pto[1]) ** 2)
geo = []
pto = ler()
geo = conv(pto)
print('latitude: {0}º, longitude: {1}º, altitude: {2}m'.format(geo[0], geo[1],  geo[2]))

# Nota: 1.0
# Excelente
