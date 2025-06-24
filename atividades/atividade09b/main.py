"""
# TODO - atividade: Crie um programa que receba os dados de dois objetos
diferentes da mesma classe Pessoa. Os dados serão os seguintes:

- Nome
- Idade
- E-mail
- Telefone
- Gênero
- Tipo Sanguíneo
- Já teve doença transmitida por sangue?

Suponha que o objeto 'usuario_2' esteja precisando de doação de sangue
do 'usuario_1'. O programa deve informar os dados dos dois usuários, e ao
final, informar se o usuario_1 pode doar sangue para o usuario_2 ou não.

# NOTE - as duas últimas perguntas deverão ter uma resposta randômica.
"""

import random

class Pessoa:# I am creating a new type of objetct called Pessoa
    def __init__(self,nome, idade, email, telefone, genero, tipo_sanguineo, doença_sanguinea ): #This is the birth function, whenever the class Pessoa #starts this object must have this attributes
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone