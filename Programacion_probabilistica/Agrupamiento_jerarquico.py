import random

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
        i = 0
        clust = {}
        for i in range(len(coordenadas)):
            distancias = []
            coord2 = []
            for j in range(len(coordenadas)):
                if i == j:
                    continue
                else:
                    distancia = Distancia(coordenadas[i][0], coordenadas[j][0], coordenadas[i][1], coordenadas[j][1])
                    print(f"""
                    x1 = {coordenadas[i][0]} , x2 ={coordenadas[j][0]}, 
                    y1 = {coordenadas[j][1]}, y2 = {coordenadas[j][1]}, distancia = {distancia} 
                    """)
                    if distancia == 0:
                        continue
                    else:
                        distancias.append(distancia)
                    j += 1
            min_distancia_j = distancias.index(min(distancias))
            min_distancia = min(distancias)
            nuevas_coord = [(coordenadas[i][0] + coordenadas[min_distancia_j][0]) / 2, (coordenadas[i][1] + coordenadas[min_distancia_j][1]) / 2]
            print(f" x = {coordenadas[i][0]} + x2 = {coordenadas[min_distancia_j][0]} ")
            print(nuevas_coord)
            clust[str(nuevas_coord)] = min_distancia
            i += 1
        print(clust)
        return clust

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