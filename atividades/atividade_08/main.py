'''
#todo - atividade crie um programa onde o usuario possa escolher as seguintes operações:
-calcular área de um quadrado
-calcular área de um retângulo
-calcular área de um triângulo
-calcular área de um trapézio
-sair do programa
#note - o usuario deverá escolher a operação em um menu
#note - o programa deverá ser feito com funções
'''

import math as m
import os


def calcular_área_de_um_quadrado():
    lado = float(input("digite o valor do lado do quadrado: "))
    area = lado**2
    print(f"a area do quadrado é {area:.2f}")
   
def calcular_área_de_um_retangulo():
    base = float(input("digite o valor da base do retangulo: "))
    altura = float(input("digite o valor da altura do retangulo: "))
    area = base*altura
    print(f"a área do retangulo é {area:.2f}") 
   
def calcular_área_de_um_triangulo():
    base = float(input("valor da base do triangulo: "))
    altura = float(input("altura do triangulo: "))
    area = (base*altura)/2
    print(f"a área do tringulo é {area:.2f}")
   
def calcular_área_de_um_trapezio():
    base_maior = float(input("digite o valor da base maior do trapezio"))
    base_menor = float(input("digite o valor da base menor do trapezio"))
    altura = float(input("digite o valor da altura do trapezio"))
    area = ((base_maior + base_menor) * altura) /2
    print(f"a área do trapézio é: {area:.2f}")

def menu():
    while True:
        print("menu")
        print("1 calcular_área_de_um_quadrado")
        print("2 calcular_área_de_um_retangulo")
        print("3 calcular_área_de_um_triangulo")
        print("4 calcular_área_de_um_trapezio")
        print("5 sair do programa")


        opcao = input(print("escolha uma opção: "))

        if opcao == '1':
            calcular_área_de_um_quadrado()
        if opcao == '2':
            calcular_área_de_um_retangulo()
        if opcao == '3':
            calcular_área_de_um_triangulo()
        if opcao == '4':
            calcular_área_de_um_trapezio()
        if opcao == '5':
            print("Bye")
            break
        else:
            print("opção inválida. Tente novamente")








