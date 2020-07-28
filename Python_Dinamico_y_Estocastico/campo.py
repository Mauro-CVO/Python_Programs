### Donde se movera el borracho

class Campo:

    def __init__(self):
        self.coordendas_de_los_borrachos = {}
    
    def add_borracho(self, borracho, coordenda):
        self.coordendas_de_los_borrachos[borracho] = coordenda

    def move_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordendas_de_los_borrachos[borracho]
        nueva_coordenada = coordenada_actual.move(delta_x, delta_y)

        self.coordendas_de_los_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):

        return self.coordendas_de_los_borrachos[borracho]