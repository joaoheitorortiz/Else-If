n = float(input("Informe sua venda mensal:"))

if (n >= 100000):
    n2 = 700 + (0.16 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
elif (n >= 80000 and n < 100000):
    n2 = 650 + (0.14 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
elif (n >= 60000 and n < 80000):
    n2 = 600 + (0.14 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
elif (n >= 40000 and n < 60000):
    n2 = 550 + (0.14 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
elif (n >= 20000 and n < 40000):
    n2 = 500 + (0.14 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
elif (n < 20000):
    n2 = 400 + (0.14 * n)
    print("Comissão que deverá ser paga ao vendedor é:",n2)
