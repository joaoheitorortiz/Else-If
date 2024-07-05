a =int(input("Digite o número referente á 'a': "))
b =int(input("Digite o número referente á 'b': "))
c =int(input("Digite o número referente á 'c': ")) 

if a != 0:
    X = (b **2) - (4 * a * c)
    if X < 0:
        print ("Não existe raiz")
    elif X == 0:
        Y = -b / (2 * a)
        print(f"{Y}, raiz única")
    elif X > 0:
        Y1 = (-b + X ) / (2 * a)
        Y2 = (-b - X ) / (2 * a)
        print(f"{Y1}, para soma e {Y2} para subtração, duas raizes")
else:
    print("Não é equação de segundo grau!!")