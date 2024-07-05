n1 =int(input("Digite a distância em Km: "))
n2 =int(input("Digite a quantidade de gasolina que o carro consumiu: "))

n3 =n1 / n2

if n3 < 8:
    print("Venda o carro")
elif n3 >= 8 and n3 <= 14:
    print("Econômico!")
else: 
    print("Super econômico!")