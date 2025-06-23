# TODO
"""
crie um progama que recebe nome ,idade e  a altura do usuario,e verifica se o usuario tem a idade
e a altura minima para entrar no bloqueio. caso não tenha,o progama devera barra a entrada do usuario.
"""

# declaraçaõ de variaveis
nome = input("informe o nome do usuário:")
idade = int(input("informe a idade do usuário:"))
altura = float(input("informe a altura do usuário:").replace(",","."))

# verifica a idade e altura do usuário
if idade >= 12 and altura >= 1.10 :
    print (f"A entrada de {nome} foi autorizada")
else:
    print(f"A entrada de {nome} foi negada")


