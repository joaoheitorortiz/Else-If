n = [ "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
n2 = int(input("Digite um número da semana: "))

if n2 >= 1 and n2 <= 7:
    print("O dia da semana representado pelo número digitado é:", n[n2 - 1])
else:
    print("Número invalido")