nome = input("informe seu nome")
idade = int(input("informe sua idade"))
#  ternario
result = "é maior de idade." if idade >= 18 else "é menor de idade."
# saida de dados
print(f"{nome} {result}")
