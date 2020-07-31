# #Crear funciones en python
# def imprimir_mensaje():
#     print("Mensaje especial:")
#     print("!Estoy aprendiendo a usar funciones!")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# #### Mi forma ####
# #Función
# def conversacion(x):
#     print("Hola")
#     print("Cómo estas ?")
#     print("Elegiste la opción " + x)
#     print("Adios")

# #Usuario elige su opción
# opcion = input("Elige una opción (1, 2, 3):")

# #Mensaje mostrado al usuario
# conversacion(x = opcion)


### Instructor ###

#Función
def conversacion(x):
    print("Hola")
    print("Cómo estas ?")
    print("Elegiste la opción " + x)
    print("Adios")

#Usuario elige su opción
opcion = int(input("Elige una opción (1, 2, 3): "))

#Print del mensaje
if opcion == 1:
    conversacion(x = str(opcion))
elif opcion == 2:
    conversacion(x = str(opcion))
elif opcion == 3:
    conversacion(x = str(opcion))
else:
    opcion = input("Debes elegir entre (1, 2, 3): ")
    conversacion(x = str(opcion))


