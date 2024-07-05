n = input("Informe seu sexo com M para Masculino e F para feminino:")
n2 = float(input("Informe sua altura"))

if n == "M":
    print("seu peso ideal é, ", (n2 * 27.7) -58)
elif n == "F":
    print("seu peso ideal é, ", (n2 * 62.1) -44,7)
else:
    print("Sexo invalido")