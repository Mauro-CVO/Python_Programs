## Programa convesor de dolares a pesos mexicanos

#Equivalencia del dolar en pesos 
peso = 0.044 #dolares

#Obtener Pesos
dolares = input("¿Cuantos dolares (USD) tienes?:")
dolares = float(dolares)

#Conversión a dolar
pesos = round(dolares / peso, 2)
pesos = print("Tienes $"+ str(pesos) + " pesos")