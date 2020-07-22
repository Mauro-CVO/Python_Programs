import random

def merge_sort1(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        merge_sort1(izquierda)
        merge_sort1(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para lalista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 5)

    return lista
    
    


# def run():
#     size = int(input("¿De que te tamaño es la lista?: "))

#     lista = [random.randint(0,100) for i in range(size)]
#     print(lista)
#     print('-' * 20)

#     sorted_list = merge_sort(lista)
#     print(sorted_list)

if __name__ == "__main__":
    size = int(input("¿De que te tamaño es la lista?: "))

    lista = [8, 4, 6, 2]
    # lista = [random.randint(0,100) for i in range(size)]
    print(lista)
    print('-' * 20)

    sorted_list = merge_sort1(lista)
    print(sorted_list)