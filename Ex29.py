n1 =int(input("Digite sua idade: "))
n2 =int(input("Digite os anos trabalhados: "))

if n1 >= 65 or n2 >= 30 or (n1 >= 60 and n2 >= 25):
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")