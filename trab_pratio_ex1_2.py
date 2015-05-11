import math

def lerPonto ():
    return input("digite um ponto no formato (x,y): ").split(',')
    

def dist(p1,  p2):
    return math.sqrt((float(p1[0]) - float(p2[0])) ** 2 + (float(p1[1]) - float(p2[1])) ** 2)

def maiorDist (pts):
    m  = 0
    for i in range(len(pts)):
        for j in range(i+1,  len(pts)):
            if dist(pts[i], pts[j]) > m:
                m = dist(pts[i], pts[j])
    return m

pts = []
for i in range(int(input('quantidade de pontos: '))):
    pts.append(lerPonto())
print('a maior distancia eh {0}'.format(maiorDist(pts)))
