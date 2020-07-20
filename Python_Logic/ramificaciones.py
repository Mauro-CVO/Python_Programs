def run():
    num_1 = int(input("Escribe el primer número: "))
    num_2 = int(input("Escribe el segundo número: "))

    if num_1 > num_2:
        print(f"{str(num_1)} es mayor que {str(num_2)}.")
    elif num_1 < num_2:
        print(f"{str(num_1)} es menor que {str(num_2)}.")
    else:
        print(f"{str(num_1)} y {str(num_2)} son iguales.")

if __name__ == "__main__":
    run()

