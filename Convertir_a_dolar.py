## Programa convesor de pesos mexivanos a dolares
menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos (MXN)
2 - Pesos colombianos (COP)
3 - Pesos argeninos (ARS)

"""
print(menu)

moneda = int(input("Elige tu moneda:"))
#Equivalencia del dólar en pesos colombianos

if moneda == 1:
    dolar = 22.54 #MXN
    tipo_moneda = "pesos mexicanos (MXN)"
elif moneda == 2:
    dolar = 3638.57 #COP
    tipo_moneda = "pesos colombianos (COP)"
else:
    dolar = 71.47 #ARS
    tipo_moneda = "pesos argentinos (ARS)"

#Obtener Pesos
pesos = input("¿Cuantos " + tipo_moneda + " tienes?:")
pesos = float(pesos)

#Conversión a dolar
dolares = round(pesos / dolar, 2)
dolares = print("Tienes $"+ str(dolares) + " dolares")