def aprox():
    num = int(input("Escoge un número entero: "))
    epsilon = 0.01
    paso = epsilon ** 2
    ans = 0.0

    while abs(ans ** 2 - num) >= epsilon and ans <= num:
        print(abs(ans ** 2 - num), ans)
        ans += paso

    if abs(ans ** 2 - num) >= epsilon:
        print(f"No se encontro la raíz cuadrada de {num}")
    else:
        print(f"La raíz cuadrada de {num} es {ans}")


if __name__ == "__main__":
    run()