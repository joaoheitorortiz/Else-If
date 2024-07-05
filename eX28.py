print("1- Soma de 2 números")
print("2- Diferença entre dois números")
print("3- Produto entre 2 números")
print("4- Divisão entre 2 números")
opcões = float(input("Digite uma das opções:"))

if (opcões == 1):
    print("Informe dois números para somar:")
    n1 = float((input("Primeiro número:")))
    n2 = float(input("Segundo número:"))
    soma = n1 + n2
    print("A soma dos dois números fica:",soma)
elif (opcões == 2):
    print("Informe dois números para subtrair:")
    n3 = float(input("Primeiro número:"))
    n4 = float(input("Segundo número:"))
    subtracao = n3 - n4
    print("A substração dos dois números fica:",subtracao)
elif (opcões == 3):
    print("Informe dois números para multiplicar:")
    n5 = float(input("Primeiro número:"))
    n6 = float(input("Segundo número:"))
    multiplicacao = n5 * n6
    print("A multiplicação dois dois números fica:",multiplicacao)
elif (opcões == 4):
    print("Informe dois números para dividir:")
    n7 = float(input("Primeiro número:"))
    n8 = float(input("Segundo número:"))
    divisao = n7/n8
    print("A divisão dos dois números é:",divisao)