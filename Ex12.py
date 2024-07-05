n1 =int(input("Digite um numero: "))
n2 =int(input("Digite outro numero: "))

if n1 > n2:
    n3 = n1 - n2
    print(f"O número {n1} é maior que {n2} por {n3} de diferença!")
elif n2 > n1:
    n3 = n2 - n1
    print(f"O número {n2} é maior que {n1} por {n3} de diferença!")
else: 
    print("Os números são iguais!")