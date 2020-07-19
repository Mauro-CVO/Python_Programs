def run():
    #Input del nombre mas fx que elimina espacios inecesarios
    name = input("¿Cual es tu nombre?: ").strip() 
    l_name = str(len(name))
    print(f"Hola {name}. Tu nombre tiene {l_name} letras")

    
if __name__ == "__main__":
    run()