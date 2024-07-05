n1 =int(input("Digite o comprimento de um lado do trângulo: "))
n2 =int(input("Digite o comprimento do outro lado do trângulo: "))
n3 =int(input("Digite o comprimento da base do triângulo: "))

if (n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2)):
    if n1 == n2 and n1 == n3 and n2 == n3:
        print("O triângulo é equilátero")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Não é triangulo")
