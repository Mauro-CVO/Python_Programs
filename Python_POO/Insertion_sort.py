import random

def insertion_sort(lista):
    # sorted = lista[0]
    # sorted_list = []
    # sorted_list.append(sorted)
    # lista.remove(sorted)
    
    # print(f"ordenada : {sorted_list}, desordenada {lista}")
    # print(sorted)

    print(range(1, len(lista)))
    
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        position = i

        while position > 0 and lista[position - 1] > valor_actual:
            lista[position] = lista[position - 1]
            position -= 1
        
        lista[position] = valor_actual
    
    return lista



def run():
    size = int(input("¿De que te tamaño es la lista?: "))

    lista = [random.randint(0,100) for i in range(size)]
    print(lista)

    sorted_list = insertion_sort(lista)
    print(sorted_list)

if __name__ == "__main__":
    run()