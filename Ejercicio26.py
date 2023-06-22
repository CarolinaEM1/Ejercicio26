#Hacer un programa que pida la anchura y altura de un rectangulo y con ayuda de una función lo dibuje con astersicos

def dibujar(ancho,alto):
    for i in range(alto):
        for i in range(ancho):
            print("* ",end="")
        print()

alto = int(input("Digite el alto del recangulo -> "))
ancho = int(input("Digite el ancho del recangulo -> "))

print()
dibujar(ancho,alto)

#Carolina EM