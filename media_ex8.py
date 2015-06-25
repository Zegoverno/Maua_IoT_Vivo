def media(notas):
    t = 0
    for nota in notas:
        t += nota
    return t / len(notas)

def maiornota(notas):
    m = 0
    for nota in notas:
        if nota > m:
            m = nota
    return m
    
notas = []
nota = 0
while True:
    try:
        nota = float(input("digite uma nota: "))
    except :
        print('voce nao digitou um numero')
        continue
    if nota < 0:
        break
    notas.append(nota)
print('Media: ',  media(notas))
print('Maior nota: ', maiornota(notas))

#Nota: 1.2 
#Comentario: valia um, mas dei +0.2 pela elegancia da solucao
