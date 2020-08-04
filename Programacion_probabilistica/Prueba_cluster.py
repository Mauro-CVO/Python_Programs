import random

def Punto_medio(x,x2,y,y2):
    return [[(x + x2) / 2], [(y + y2)/ 2]]



def Distancia(x,x2, y, y2):
    distancia = ((x - x2) ** 2 + (y - y2) ** 2) ** .5
    print(f"def dist x = {x}, x2 = {x2}, y = {y}, y2 = {y2}")
    return distancia


def clust_dict(clust):
    items_clust = clust.items()
    pass



def clustering(coordenadas):

    if len(coordenadas) == 1:
        print(coordenadas)

    # elif len(coordenadas) == 2:
        # distancia = Distancia(coordenadas[0][0], coordenadas[0][1], coordenadas[1][0], coordenadas[1][1])
        # clust = distancia / 2
        # print(clust)

    else:
        clust = {}

        for i in range(len(coordenadas) - 1):
            distancias = {}
            a = coordenadas[i]

            for coordenada in coordenadas:

                distancia = Distancia(a[0], coordenada[0], a[1], coordenada[1])
                medio = Punto_medio(a[0], coordenada[0], a[1], coordenada[1])
                if distancia == 0:
                    continue
                else:   
                    distancias[str(medio)] = distancia


        min_distancia = min(distancias.items(), key= lambda x: x[1])
        coordenadas.append()




def run():
    coordenadas = []
    n = int(input("Número de puntos: "))

    for i in range(n):
        x = random.randint(1,20)
        y = random.randint(1,20)
        coordenadas.append([x,y])

    print(coordenadas)

    clustering(coordenadas)



if __name__ == "__main__":
    run()