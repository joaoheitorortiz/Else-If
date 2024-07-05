n1 =int(input("Digite o código do produto: "))
n2 =int(input("Digite a quantidade de pedidos desse produto: "))

if n1 == 100:
    n3 = n2 * 12.00
    print(f"O preço final do produto é: {n3}")
elif n1 == 102:
    n3 = n2 * 18.50
    print(f"O preço final do produto é: {n3}")
elif n1 == 103:
    n3 = n2 * 25.50
    print(f"O preço final do produto é: {n3}")
elif n1 == 104:
    n3 = n2 * 17.00
    print(f"O preço final do produto é: {n3}")
elif n1 == 105:
    n3 = n2 * 9.50
    print(f"O preço final do produto é: {n3}")
elif n1 == 106:
    n3 = n2 * 6.00
    print(f"O preço final do produto é: {n3}")
else:
    print("Este código não existe!!")