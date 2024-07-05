import time

n =int(input("Digite um numero: "))

if n >= 0:
    y = n ** 2
    print(f"O quadrado de {n} é {y}")
    time.sleep(1)

    x = n ** (1/2)
    print(f"A raiz quadrada de {n} é {x}")
else: 
    print("Número negativo!!")
    