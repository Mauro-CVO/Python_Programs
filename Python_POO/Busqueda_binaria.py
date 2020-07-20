def busqueda_binaria():
    num = int(input("Escoge un número: "))
    epsilon = float(input("¿De que tamaño quieres epsilon?: "))
    bajo = 0.0
    alto = max(1.0, num)
    ans = (alto + bajo)/2

    while abs(ans ** 2 - num) >= epsilon:
        print(f"{bajo} = bajo, {alto} = alto, {ans} = answer")
        if ans ** 2 < num:
            bajo = ans
        else:
            alto = ans

        ans = (alto + bajo) / 2

    print(f"La raíz cuadrada de {num} es {ans} aproximadamente")
    print(f"Disminuye el valor de epsilon para aproximarte cada vez más al valor real.")
    
def aprox():
    num = int(input("Escoge un número entero: "))
    epsilon = float(input("¿De que tamaño quieres epsilon?: "))
    paso = epsilon ** 2
    ans = 0.0

    while abs(ans ** 2 - num) >= epsilon and ans <= num:
        print(abs(ans ** 2 - num), ans)
        ans += paso

    if abs(ans ** 2 - num) >= epsilon:
        print(f"No se encontro la raíz cuadrada de {num}")
    else:
        print(f"La raíz cuadrada de {num} es {ans} aproximadamente")
        print(f"Disminuye el valor de epsilon para aproximarte cada vez más al valor real.")

def enumeracion_exhaustiva():
    num = int(input("Escoge un entero: "))
    ans = 0

    while ans ** 2 < num:
        ans += 1

    if ans ** 2 == num:
        print(f"La raíz cuadrada de {num} es {ans}")
    else:
        print(f"{num} no tiene raiz cuadrada exacta")


def run():
    print("""Bienvenido. Aquí podrás saber la raíz cuadrada de cualquier número. 
    Elige el Método que quieras usar.""")
    metodo = int(input(""" 
    1 - Enumeración Exhaustiva (Solo para numeros con raices reales).
    2 - Aproximación
    3 - Busqueda Binaria
    Tu opción:  """))

    if metodo == 1:
        enumeracion_exhaustiva()
    elif metodo == 2:
        aprox()
    elif metodo == 3:
        busqueda_binaria()
    else:
        print("Elige una opción correcta!!!!!!!")
        run()

if __name__ == "__main__":
    run()
    