def enumeracion_exhaustiva():
    num = int(input("Escoge un entero: "))
    ans = 0

    while ans ** 2 < num:
        ans += 1

        if ans ** 2 == num:
            print(f"La raíz cuadrada de {num} es {ans}")
        else:
            print(f"{num} no tiene raiz cuadrada exacta")



if __name__ == "__main__":
    run()