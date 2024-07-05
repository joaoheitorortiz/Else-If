n = int(input("Digite o ano: "))

if n % 4 == 0 and n % 100 != 0:
    print(f"O ano {n} é bissexto!!")
else:
    print(f"o ano {n} não é bissexto!!")