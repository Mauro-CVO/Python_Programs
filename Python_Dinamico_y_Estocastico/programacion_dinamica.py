import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Intercambio de tiempo por espacio, para optimizar el algortio
# para el numero de fibonacci

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        ans = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n -2, memo)
        memo[n] = ans

        return ans


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input(":"))
    ans = fibonacci_dinamico(n)
    print(ans)