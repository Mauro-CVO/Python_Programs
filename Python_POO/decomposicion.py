## Modelado de un AutoMóvil

class Auto:

    def __init__(self, modelo, marca, color, gasolina = 40):
        self.modelo = modelo
        self.marca = marca
        self.color = color        
        self.gasolina = gasolina
        self._estado = "apagado"
        self._motor = Motor(cilindros = 4)
        print(self.gasolina)

    def encender(self):
        self._motor._temperatura = 50
        self._estado = "encendido"
        print("Carro Encendido")

    def acelerar(self, tipo = "despacio"):
        
        if self._estado == "apagado":
            self._motor.error = "apagado"
            self._motor.alerta()
        else:
            if tipo == "despacio":
                if self.gasolina >= 5:
                    self.gasolina = self.gasolina - 5
                    print("Arrancando")
                else:
                    self._motor.alerta()
            else:
                if self.gasolina >= 10:
                    self.gasolina = self.gasolina - 10
                    print("Arrancando")
                else:
                    self._motor.alerta()

    def frenar(self):
        if self._estado == "apagado":
            return self._motor.alerta()
        else:
            self._estado= "frenando"
            self._motor._temperatura = 80
            print("frenando")

    def apagar(self):
        self._estado = "apagado"
        self._motor._temperatura = 50
        print("coche apagado")
    
    def info(self):
        print(f"El cohe está {self._estado}")
        print(f"Hay {self.gasolina}L de gasolina")

class Motor:

    def __init__(self, cilindros, error = "Gasolina"):
        self.cilindros = cilindros
        self._temperatura = 0
        self.error = error
    
    def alerta(self):
        if self.error == "Gasolina":
            print("Sin Gasolina")
        else:
            print("Coche apagado")
    


if __name__ == "__main__":
    
    car = Auto(modelo = 2 , marca = "Audi", color = "Rojo" , gasolina = 20)
    car.encender()
    car.acelerar()
    car.acelerar(tipo = "rapido")
    car.acelerar(tipo = "rapido")
    car.info()
    
    
    

