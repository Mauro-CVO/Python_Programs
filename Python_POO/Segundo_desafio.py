#Creado por MAU
def run():
    print("""Hola, ¿quieren saber quien es mayor?""")
    num = int(input("Primero necesito saber cuantos son: "))
    print("Ahora necesito saber sus nombres y edades...")
    #Creamos tuplas vacías para despues usarlas
    names = []
    ages = []

    if num == 1:
        print("Error: #404 not Found")
        #Ciclo for para preguntar todos los nombres
    else:
        for i in range (num):
            name = input("¿Como te llamas?: ").strip()
            name = name.capitalize()
            age = int(input("¿Cuantos años tines?: "))
            names.append(name)
            ages.append(age)

    #Nos dice en que posición está el número más grande de la tupla
    index_age = ages.index(max(ages))
    #Elegimos con el index a la persona más grande
    older = names[index_age]
    print(f"{older} es el mayor")

if __name__ == "__main__":
    run()