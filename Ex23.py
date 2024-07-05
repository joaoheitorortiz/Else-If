n = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
n2 = int(input("Digite um número do mês: "))

if n2 >= 1 and n2 <= 12:
    print("O dia da semana representado pelo número digitado é:", n[n2 - 1])
else:
    print("Número invalido")