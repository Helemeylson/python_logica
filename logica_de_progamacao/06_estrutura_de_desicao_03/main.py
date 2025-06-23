"""
crie um progama que receba o nome e a média final de um aluno,
e o progama retorna se o aluno foi aprovado,se ficou de recuperação,
ou se foi reprovado,com base em sua média final.
"""
# TODO
# NOTE - a média deverá ser entre 0 e 10.
# declaração de variáveis

nome =input("nforme o nome do aluno")
media = float(input("informe  média do aluno").replace(",","."))

# verifica se a média esta dentro do intervalo.
if media >= 0 and media <=10:
    if media >= 7:
        print(f"{nome} esta aprovado")
    elif media >= 5 :
        print(f"{nome} esta de recuperação")
    else:
        print(f"{nome} esta reprovado")
else:
    print("valor da média inválida")


