## Funciones
def palindromo(palabra):
    palabra = palabra.replace(" ","") #Elimina espacios
    palabra = palabra.lower() #deja todas las letras en minus
    palindromo = palabra[::-1] #Voltea la palabra
    if palabra == palindromo:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Entry Point
if __name__ == "__main__":
    run()