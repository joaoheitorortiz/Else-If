n1 =int(input("Digite um numero: "))
n2 =int(input("Digite outro numero: "))
n3 =int(input("Digite outro numero: "))

if n2 == (n1 + 1) and n3 == (n2 + 1):
    print(f"os numeros {n1}, {n2}, {n3}, estão em ordem crescente")
else:
    print(f"os numeros {n1}, {n2}, {n3}, não estão em ordem crescente")