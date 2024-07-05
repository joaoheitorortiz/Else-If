y = int(input("Digite um numero: "))
x = int(input("Digite outro numero: "))

if y > x :
    print(f"{y}, é maior que {x}")
elif x > y:
    print(f"{x}, é maior que {y}")
else:
    print("Os valores são iguais")