## ordenamiento de burbuja

import random

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
    return lista
    
def run():
    size = int(input("¿De que te tamaño es la lista?: "))

    lista = [random.randint(0,100) for i in range(size)]
    print(lista)

    sorted_list = bubble_sort(lista)
    print(sorted_list)

if __name__ == "__main__":
    run()