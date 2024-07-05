n = float(input("Informe o custo de fabrica:"))

if (n <= 12000):
    n2 = n * 0.05
    print("A comissão do distribuidor fica:",n2)
    print("Você não precisa pagar impostos")
elif (n > 12000 and n <= 25000):
    n2 = n * 0.10
    impostos = n * 0.15
    print("A comissão do distribuidor fica:",n2)
    print("Os impostos que você deve pegar é:",impostos)
elif (n > 25000):
    n2 = n * 0.15
    impostos = n * 0.20
    print("A comissão do distribuidor fica:",n2)
    print("Os impostos você deve pegar é:",impostos)