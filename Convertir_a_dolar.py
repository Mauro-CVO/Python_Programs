# ## Programa convesor de pesos a dolares
# menu = """
# Bienvenido al conversor de monedas 💰

# 1 - Pesos mexicanos (MXN)
# 2 - Pesos colombianos (COP)
# 3 - Pesos argeninos (ARS)s
# """
# print(menu)
# #Elegir moneda
# moneda = int(input("Elige tu moneda:"))
# #Equivalencia del dólar en pesos 
# if moneda == 1:
#     dolar = 22.54 #MXN
#     tipo_moneda = "pesos mexicanos (MXN)"
# elif moneda == 2:
#     dolar = 3638.57 #COP
#     tipo_moneda = "pesos colombianos (COP)"
# elif moneda == 3:
#     dolar = 71.47 #ARS
#     tipo_moneda = "pesos argentinos (ARS)"
# else:  
#     print("Elige una opción correcta")

# pesos = float (input("¿Cuantos " + tipo_moneda + " tienes?:"))
# dolares = print("Tienes $"+ str(round(pesos / dolar, 2)) + " dolares")

#Funcion del calculo
def calculo(dolar, tipo_moneda):
    pesos = float (input("¿Cuantos " + tipo_moneda + " tienes?:"))
    dolares = print("Tienes $"+ str(round(pesos / dolar, 2)) + " dolares")
menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos (MXN)
2 - Pesos colombianos (COP)
3 - Pesos argeninos (ARS)s
"""
print(menu)
#Elegir moneda
moneda = int(input("Elige tu moneda:"))
#Equivalencia del dólar en pesos 
if moneda == 1:
    dolar = 22.54 #MXN
    tipo_moneda = "pesos mexicanos (MXN)"
    calculo(dolar, tipo_moneda)
elif moneda == 2:
    dolar = 3638.57 #COP
    tipo_moneda = "pesos colombianos (COP)"
    calculo(dolar, tipo_moneda)
elif moneda == 3:
    dolar = 71.47 #ARS
    tipo_moneda = "pesos argentinos (ARS)"
    calculo(dolar, tipo_moneda)
else:  
   print("Elige una opción correcta")