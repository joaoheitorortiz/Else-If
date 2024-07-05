n1 =int(input("Digite a nota do trabalho: "))
n2 =int(input("Digite a nota da avaliação semestral: "))
n3 =int(input("Digite a nota do exame final: "))

n11 = n1 * 2
n22 = n2 * 3
n33 = n3 * 5
n4 = (n11 + n22 + n33)/10

if n4 >= 0 and n4 < 3:
    print("O aluno está reprovado")
elif n4 >=3 and n4 < 6:
    print("O aluno está de recuperação")
else:
    print("O aluno está aprovado")
