class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.cantidad_de_combustible = 50
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
    
    def enceder(self):
        self._motor._temperatura = 30
        print(f'La temperatura del motor es de: {self._motor._temperatura}, Combustible disponible {self.cantidad_de_combustible}')

    def acelerar(self, tipo='despacio'):
        if self.cantidad_de_combustible > 0:
            if tipo == 'rapida':
                self._motor.inyecta_gasolina(10)
                self.cantidad_de_combustible = self.cantidad_de_combustible - 10
            else:
                self._motor.inyecta_gasolina(3)
                self.cantidad_de_combustible = self.cantidad_de_combustible - 3
            self._estado = 'en_movimiento'
            print(self._estado)
        else:
            self._estado = 'en_reposo'
    
    def frenar(self):
        self._estado = 'en_reposo'
    
    def girar(self,direccion_de_giro:str):
        if direccion_de_giro == "derecha":
            print("Girando a la {}".format(direccion_de_giro))
        else:
            print("Girando a la {}".format(direccion_de_giro))



class Motor:

    def __init__(self, cilindros:float, tipo:str='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

if __name__ == '__main__':
    auto = Automovil('Rio 5','Kia','Negro')
    auto.enceder()
    auto.acelerar('rapida')
    auto.girar('izquierda')
    print(auto.cantidad_de_combustible)