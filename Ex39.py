n = int(input("Informe o tamanho em metros quadrados da área a ser pintada:"))


if (n <= 108):
    print("Apenas comprando em latas de 18 litros fica:")
    n2 = 1
    print("A quantidade de latas que você precisa é:",n2)
    n3 = 80
    print("O preço que você vai pegar vai ser de:",n3)
    print("Apenas comprando em latas de 3.6 litros fica:") 
    n2 = (n * 21.6)/3.6
    print("A quantidade de tinta que você precisa em litros é de:",(n/3.6))
    n3 = n2
    print("O preço que você vai pegar vai ser de:",n3)
elif (n > 108):
    n2 = (n)/6 + 0.5
    print("A quantidade de tinta que você precisa é de:",n2)
    n3 = 80 + n2
    print("O preço que você vai pegar vai ser de:",n3)
elif (n <= 108):
    print("Apenas comprando em latas de 3.6 litros fica:") 
    n2 = (n * 3.6) 
    print("A quantidade de tinta que você precisa é de:",n2)
    n3 = 80
    print("O preço que você vai pegar vai ser de:",n3)