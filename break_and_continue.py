# Funcion imprimir numeros pares
# def run():
#     for contador in range(1000):
#         if contador %2 != 0:
#             continue
#         print(contador)

# def run():
#     for i in range(10000):
#         print(i)
#         if i == 5678:
#             break

def run():
    texto = input("Escribe un texto: ")
    for i in texto:
        if i == "o":
            break
        print(i)

if __name__ == "__main__":
    run()