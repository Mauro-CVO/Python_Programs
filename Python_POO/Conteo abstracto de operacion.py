def f(x):

    ans = 0

    for i in range (1000):  # correra 1000 veces
        ans += 1
    
    for i in range(x):  # se le suma 1
        ans += 1
    
    for i in range(x):     #se le suma x y
        for j in range(x): # se multiplica por otra x
            ans += 1       # xomo son dos operaciones en total 2x^2
            ans += 1 

    return ans # en total 1000+x+2x^2
               # el crecimiento de la función