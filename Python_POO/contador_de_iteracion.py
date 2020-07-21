import random

def busqueda_binaria(lista, comienzo, final, objetivo, contador = 0):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    print(contador)
    contador += 1

    if comienzo > final:
        return (False, contador)
  
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, contador)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador = contador)
        
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador = contador)
        


def busqueda_lineal(lista, objetivo): #objetivo = elemento que queremos encntrar
    match = False
    count = 0
    for elemento in lista:
        count += 1
        if elemento == objetivo:
            match = True
            break
    
    print(f"Número de iteraciones: {count}. Busqueda_Lineal")
    return match
    

def run():
    size = int(input("¿De que te tamaño es la lista?: "))
    objetivo = int(input("¿Que número quieres encontrar?: "))
    lista = [random.randint(0,100) for i in range(size)]
    lista2 = sorted(lista)
    print(lista)
    print(lista2)
    encontrado_bi = busqueda_binaria (lista2, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado_bi else "no esta"} en la lista')
    encontrado_lin = busqueda_lineal (lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado_lin else "no esta"} en la lista')

if __name__ == "__main__":
    run()
    