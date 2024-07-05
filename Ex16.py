n = int(input("Digite o horario trabalhado pelo funcionario: "))
n2 = n * 40.50

if n2 >= 2500.00:
    n2 = n2 * 0.89
    print(f"O salário liquido do funcionario é {n2}")
else:
    print(f"O salário liquido do funcionario é {n2}")