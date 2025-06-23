# tratamento de exceção
try:
    numero = int(input("informe um numero inteiro"))
    
    # saida de dados
    print(f"o numero informado é {numero}.")
except Exception as e:
    print(f"nao foi possivel imprimir o numero.{e}.")
finally:
    print("progama encerrado")
