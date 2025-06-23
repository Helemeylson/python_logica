num1 = float(input("informe o primeiro numero:"))
num2 = float(input("informe o segundo numero:"))

print("calculadora python menu")
print("1 soma")
print("2 subtração")
print("3 multiplicação")
print("4 divisão")
operador = input("informe a operação desejada")
match operador:
    case "1":
        print(f"a soma do resultado é {num1+{num2}}")
    case "2":
        print(f"a subtração do resultado é {num1}+{num2}:")
    case "3":
        print(f"a multiplicação do resultado é: {num1}*{num2}")
    case "4":
        print(f"a divisão do resutado é {num1}/{num2}")
    case _:
        print("operador invalido")    
