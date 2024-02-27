cervejas_artesanais_favoritas = []
qto_estilos = int(input('Quantos estilos de cervejas artesanais você gosta? '))
contador = 0
while contador < qto_estilos:
    pergunta = input(f'A {contador + 1} é:  ')
    cervejas_artesanais_favoritas.append(pergunta)
    contador += 1

print(cervejas_artesanais_favoritas)