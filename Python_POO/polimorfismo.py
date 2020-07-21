
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f"{self.nombre} está Caminando")

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(f"{self.nombre} está andando en bici")

def main():
    mauro = Persona("Mauro")
    mauro.avanza()

    luis = Ciclista("Luis")
    luis.avanza()

if __name__ == "__main__":
    main()
