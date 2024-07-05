n1 =float(input("Digite o preço: "))
n2 =input("Informe o estado de destino do produto com sua sigla: ").upper()

if n2 == "MS":
    n1 = n1 + (n1 * 0.08)
    print(f"O preço final do produto é: {n1}")
elif n2 == "MG":
    n1 = n1 + (n1 * 0.07)
    print(f"O preço final do produto é: {n1}")
elif n2 == "SP":
    n1 = n1 + (n1 * 0.12)
    print(f"O preço final do produto é: {n1}")
elif n2 == "RJ":
    n1 = n1 + (n1 * 0.15)
    print(f"O preço final do produto é: {n1}")
else:
    print("Não vendemos nesse estado!!")
