## Big O Notation
# Encuadrar los algoritmos en una clase para su comparación


#ley de la suma

def f(n):

    for i in range(n):
        print (i)
    
    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) => O(n) crecimiento lineal

def f2(n):

    for i in range(n): # O(n)
        print(i)

    for i in range(n * n): # O(n^2)
        print(i)
    
# O(n) + O(n^2) = O(n^2 + n) => O(n^2)

## Ley de multiplicación

def f3(n):  
    for i in range(n):

        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n*n) = O(n^2)

## Recursividad múltple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# O(2 ^ n)
