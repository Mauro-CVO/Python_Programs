def run():
    mi_diccionario = {
        "llave1": 1, 
        "llave2": 2,
        "llave3": 3,
    }
    
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "argentina" : 44938712,
        "brasil" : 210147125,
        "colombia" : 5037224,
    }

    # for i in poblacion_paises.keys():
    #     print(i)

    # for i in poblacion_paises.values():
    #     print(i)

    for i,x in poblacion_paises.items():
        print(i.capitalize() + " tiene: " + str(x) + " hanitantes")

if __name__ == "__main__":
    run()