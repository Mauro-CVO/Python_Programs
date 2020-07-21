
class Compra

    def __init__(self, concepto, precio, cantidad):
        self.concepto = concepto
        self.precio = precio
        self.cantidad = cantidad
        self._cuenta = {}

    def Cuenta(self):
        
        self._cuenta[]