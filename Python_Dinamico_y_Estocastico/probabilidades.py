import random

def tirar_dado(numero_de_tiros, numero_de_dados):
    secuencia_de_tiros = []

    if numero_de_dados == 1:
        for i in range(numero_de_tiros):    #lanzamientos del primer dado
            tiro = random.choice([1, 2, 3, 4, 5, 6])
            secuencia_de_tiros.append(tiro)
        return secuencia_de_tiros

    elif numero_de_dados == 2:
        for i in range(numero_de_tiros):    #lanzamientos del primer dado
            tiro = random.choice([1, 2, 3, 4, 5, 6])
            tiro2 = random.choice([1, 2, 3, 4, 5, 6])
            x = tiro + tiro2
            secuencia_de_tiros.append(x)
        return secuencia_de_tiros
    
    else:
        print("Elige una opción correcta...")
        main()


    

def run(numero_de_tiros, numero_de_intentos, numero_proba, numero_de_dados):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros, numero_de_dados)
        tiros.append(secuencia_de_tiros)
    
    tiros_con_proba = 0 #Cuenta para el número de veces que sale 12

    for tiro in tiros:
        if numero_proba in tiro:
            tiros_con_proba += 1
    
    probabilidad_de_tiros_con_proba = tiros_con_proba / numero_de_intentos
    print(f"La probabilidad de obtener por lo menos un {numero_proba} en {numero_de_tiros} tiros = {probabilidad_de_tiros_con_proba}")

def main():
    numero_de_tiros = int(input("Número de tiros: "))
    numero_de_intentos = int(input("Cuantas veces correra la simulación: "))
    numero_proba = int(input("¿ De que número quieres saber la probabilidad? :"))
    numero_de_dados = int(input("¿Número de dados? (1 o 2): "))

    run(numero_de_tiros, numero_de_intentos, numero_proba, numero_de_dados)


if __name__ == "__main__":
    main()

    
