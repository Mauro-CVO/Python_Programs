def es_primo(y):
    contador = 0

    if y == 1:
        return False
    else:
        numero_mas = y + 1
        for i in range(1, numero_mas):
            if i == 1 or i == y:
                continue
            if y % i == 0:
                contador += 1
        if contador == 0:
            return True
        else:
            return False


# def run():
#     numero = int(input("Escribe un número: "))
#     if es_primo(numero):
#         print("Es primo")
#     else:
#         print("No es primo") 


def count():
    numero = int(input("¿Hasta que número quieres hacer la prueba?: "))

    for y in range (numero):
        y += 1
        
        if es_primo(y):
            print(str(y) + " Es primo")
        else:
           print(str(y) + " No es primo")


if __name__ == "__main__":
    count()