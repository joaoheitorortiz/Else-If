n1 =int(input("Digite a base maior do trapézio: "))
n2 =int(input("Digite a base menor do trapézio: "))
n3 =int(input("Digite a altura do trapézio: "))

if n1 > n2 and n1 > 0 and n2 > 0:
    X = ((n1 + n2) * n3) / 2
    print(f"A área do trapézio é {X}")
else:
    print("Não é trapézio")