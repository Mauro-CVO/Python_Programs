
from borrachos import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.move_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre = "David")
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(intentos):
        campo = Campo()
        campo.add_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def run(distancias, intentos, tipo_de_borracho):

    for pasos in distancias:
        distancias = simular_caminata(pasos, intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias))
        distancias_max = max(distancias)
        distancias_min = min(distancias)

        print(f"{tipo_de_borracho.__name__} camino {pasos}")
        print(f"Max = {distancias_max}")
        print(f"Min = {distancias_min}")
        print(f"Mean = {distancia_media}")
        


if __name__ == "__main__":
    distancias = [10, 100, 1000, 10000]
    intentos = 100

    run(distancias, intentos, BorrachoTradicional)