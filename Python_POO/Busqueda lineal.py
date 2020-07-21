## Algoritmo de busqueda lineal
import random

def busqueda_lineal(lista, objetivo): #objetivo = elemento que queremos encntrar
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        
    return match

if __name__ == "__main__":
    size = int(input("¿De que te tamaño es la lista?: "))
    objetivo = int(input("¿Que número quieres encontrar?: "))

    lista = [random.randint(0,100) for i in range(size)]
    print(lista)

    encontrado = busqueda_lineal (lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
