import random
import collections

PALOS = ["espada", "corazon", "rombo", "trebol"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
VALORES_ESCALERA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES_ESCALERA:
            barajas.append((palo,valor))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = [] 

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares +=1
                break
    
    corrida = 0
    i = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
            valores.sort()
            # print(valores)
        if valores[i] == valores[i + 1] - 1 and valores[i + 1] == valores[i + 2] - 1 and valores[i + 2] == valores[i + 3] - 1 and valores[i + 3] == valores[i + 4] - 1:
            corrida += 1
        else:
            continue
    
    probabilidad_corrida = corrida / intentos
    print(f"La probabilidad de obtener una escalera en una mano de {tamano_mano} es de {probabilidad_corrida}")

        
    probabilidad_par = pares / intentos
    print(f"La probabilidad de obtener un par en una mano de {tamano_mano} es de {probabilidad_par}")
    





if __name__ == "__main__":

    tamano_mano = int(input("¿De cuantas cartas sera la mano?: "))
    intentos = int(input("Número de intentos: "))

    main(tamano_mano, intentos)
