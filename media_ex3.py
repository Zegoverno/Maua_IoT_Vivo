def media(notas):
    t = 0
    for nota in notas:
        t += nota
    return t / len(notas)
    
notas = []
nota = 0
while True:
    nota = float(input("digite uma nota: "))
    if nota < 0:
        break
    notas.append(nota)
print('Media: ',  media(notas))

# Nota: 1.0
# Comentario: muito bom
