"""
crie um progama que receba do usuario dois numeros reais,
e uma das 4 operações da matematica informadas pelo usuario,e faça o calculo correspondente.
"""
num1 = float(input("Digite o primeiro numero desejado: "))
num2 = float(input("Digite o segundo número desejado: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == '/':
   
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")