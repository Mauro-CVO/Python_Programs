# 01 knap sack

def morral(size, weigths, valores, n):
    print(f"valores[n] {valores[n-1]}")
    print(f"size = {size}")

    if n == 0 or size == 0:
        return 0
    
    if weights[n - 1] > size:
        return morral(size, weights, valores, n - 1)

    print(valores[n - 1])
    return max(valores[n - 1] + morral(size - weights[n - 1], weights, valores, n-1),
                morral(size, weights, valores, n - 1 ))



if __name__ == "__main__":
    valores = [60, 100, 120]
    weights = [10, 20, 30]
    size = 30
    n = len(valores)

    ans = morral(size, weights, valores, n)
    print(ans)