import random

def intento():
    x = input("""
¿Quieres intertarlo de nuevo?: [si/no] 
            """)

    if x != "si" and x != "no":
        print("Elige una opción correcta")
        intento()
    elif x == "si":
        return 1
    else:
        return 0


def juego(n, vidas):
    i = 1
    while vidas > 0:
        res = int(input(f"{n} * {i} = "))
        if res == n * i:
            print(random.choice(["Excelente","Muy bien", "Bien Hecho"]))
            # print(f"{n} * {i} = {n * i}")
            i += 1
        else:
            print("")
            print(f"Intentalo de nuevo")
            vidas -= 1
            print("")
            if vidas == 1:
                print(f"Te queda {vidas} vida")
                print("")
            else:
                print(f"Te quedan {vidas} vidas")
                print("")

        if vidas == 0:
            play_again = intento()
            if play_again == 1:
                juego(n , 3)
            else:
                print("Hasta la proxima")

        if i == 11:
            print("Haz Ganado")
            break


def run():
    vidas = 3
    n = int(input("""
    Bienvenido, con este juego aprenderas a multiplicar.
    ¿Con que número quieres practicar?: """))


    if n < 0:
        print("El número debe ser positivo. Intenta de nuevo")
        run()
    else:
        print("Que empieze el juego!!")
        juego(n, vidas)
    

if __name__ == "__main__":
    run()
