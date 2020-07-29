import random

def media(X): 
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu) ** 2

    return acumulador / len(X)

def desvest(X):
    return (varianza(X)) ** .5

if __name__ == "__main__":
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desvest(X)

    print(f"X = {X}")
    print(f"Media = {mu}")
    print(f"Var = {Var}")
    print(f"sigma = {sigma}")

