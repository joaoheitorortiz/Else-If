y = float(input("Digite um numero: "))
x = float(input("Digite outro numero: "))

if (y > 0 and y <= 10) and (x > 0 and x <= 10):
    z = (y + x)/2
    print(f"A nota do Aluno é {z}")
else:
    print("Nota invalida")