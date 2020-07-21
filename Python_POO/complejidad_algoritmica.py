import time
import sys

#Factorial, implementación iterativa
def factorial(n):
    ans = 1

    while n > 1:
        ans *= n
        n -= 1

    return ans 

#Factorial, implementación recursiva
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

def recus_lim(lim = 5000):
    sys.setrecursionlimit(lim)
    print(sys.getrecursionlimit())


if __name__ == "__main__":
    recus_lim()

    n = 4000

    # comienzo = time.time()
    # factorial(n)
    # final = time.time()
    # print(final - comienzo)

    comienzo = time.time()
    print(factorial_r(n))
    final = time.time()
    print(final - comienzo)