n = float(input("Informe o preço antigo:"))

if (n <= 50):
    n2 = n + (n * 0.05)
    print("Produto teve aumento de 5%, valor novo ficou:",n2)
elif (n > 50 and n <= 100):
    n2 =  n + (n * 0.10)
    print("Produto teve aumento de 10%, valor novo ficou:",n2)
elif (n > 100):
     n2 =  n + (n * 0.15) 
     print("Produto teve aumento de 10%, valor novo ficou:",n2)
           