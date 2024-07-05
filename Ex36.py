n = float(input("Informe seu salário atual:"))
n2 = float(input("Informe seu tempo se serviço em anos na empresa:"))

if (n <= 500 and n2 <= 1):
    n3 = n + (n * 0.25)
    print("Seu salario após os reajustes ficou:",n3)
    print("Você não tem bônus por tempo de serviço")
elif (n <= 1000 and n2 > 1 or n2 <= 3):
    n3 = n + (n * 0.20)
    n4 = n3 + 100
    print("Seu salario após os reajustes ficou:",n3,"e seu bônus por tempo de serviço ficou:",n4)
elif (n <= 1500 and n2 >= 4 or n2 <= 6):
    n3 = n + (n * 0.15)
    n4 = n3 + 200
    print("Seu salario após os reajustes ficou:",n3,"e seu bônus por tempo de serviço ficou:",n4)
elif (n <= 2000 and n2 >= 7 or n2 <= 10 ):
    n3 = n + (n * 0.10)
    n4 = n3 + 300
    print("Seu salario após os reajustes ficou:",n3,"e seu bônus por tempo de serviço ficou:",n4)
elif (n > 2000 and n2 > 10):
    n4 = n + 50
    print("Você não tem reajuste de salário, mas seu bônus por tempo de serviço ficou:",n4)
                 