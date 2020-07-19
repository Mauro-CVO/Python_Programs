# Recorrido hacia abajo e izquierda
# #Funcion 
# def run():
#     nombre = input("Escribe tu nombre: ")
#     nombre = nombre.strip()
#     x = 0
#     y = len(nombre)
    
#     for letra in nombre:
#         print(nombre[x:y])
#         x += 1

# Recorrido hacía abajo en MAYUS
def run():
    frase = input("Escribe una frase: ")
    for i in frase:
        print(i.upper())


if __name__ == "__main__":
    run()