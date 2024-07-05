n =int(input("Digite o valor da aquisição: "))

if n <= 50:
    n = n * 1.45
    print(f"O produto sera vendido por {n}!!")
else:
    n = n * 1.30
    print(f"O produto sera vendido por {n}!!")