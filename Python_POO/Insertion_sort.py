import random

def insertion_sort(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        position = i
        print(f"i ={i}")
        print(f"{valor_actual} valor actual, {position} posición")

        while position > 0 and lista[position - 1] > valor_actual:
            lista[position] = lista[position - 1]
            position -= 1
            print(f"{lista} lista pre, {position} posicion")
        
        lista[position] = valor_actual
        print(f"{lista[position]} = list.pos, {lista} = lista")
        
    print()
    return lista



def run():
    size = int(input("¿De que te tamaño es la lista?: "))
    lista = [random.randint(0,100) for i in range(size)]
    print(lista)

    sorted_list = insertion_sort(lista)
    print(sorted_list)

if __name__ == "__main__":
    run()