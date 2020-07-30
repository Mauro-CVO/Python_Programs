import random
from estaditicas import desvest, media

def aventar_agujas(num_agujas):
    dentro_circulo = 0

    for _ in range(num_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_centro = (x ** 2 + y ** 2) ** 0.5

        if distancia_centro <= 1:
            dentro_circulo += 1
        
    return (4 * dentro_circulo)/ num_agujas

def estimacion(num_agujas, num_intentos):
    estimados = []
    for _ in range(num_intentos):
        estimacion_pi = aventar_agujas(num_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = media(estimados)
    sigma = desvest(estimados)
    print(f"Estimado: {round(media_estimados, 5)}, sigma: {round(sigma, 5)} con {num_agujas} agujas")

    return(media_estimados, sigma)

def estimar_pi(precision, num_intentos, num_agujas):
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(num_agujas, num_intentos)
        num_agujas *=  2
    
    return media
    
    
if __name__ == "__main__":

    num_intentos = int(input("¿Número de intentos?: "))
    num_agujas = int(input("¿Numero de agujas?: "))
    precision = float(input("Precisión: "))
    estimar_pi(precision, num_intentos, num_agujas)