#Busqueda Binaria
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == "__main__":
    size = int(input("¿De que te tamaño es la lista?: "))
    objetivo = int(input("¿Que número quieres encontrar?: "))

    lista = sorted([random.randint(0,100) for i in range(size)])
    print(lista)

    encontrado = busqueda_binaria (lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')