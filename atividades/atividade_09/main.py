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

class Pessoa: # i am cratin a new type of object called Pessoa
    def __init__(self, nome, idade, email, telefone, genero, tipo_sanguineo, doenca_sanguinea): #this is a constructor, it takes the information
        #and stores it in the object
        self.nome = nome #self is the instruction to method
        self.idade = idade # this is the object saying this is my own/self name
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo
        self.doenca_sanguinea = doenca_sanguinea

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Gênero: {self.genero}")
        print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
        print(f"Já teve doença transmitida por sangue? {'Sim' if self.doenca_sanguinea else 'Não'}")
        print("-" * 40)

# Regras básicas de compatibilidade sanguínea (simplificadas)
def pode_doar(tipo_doador, tipo_receptor):
    compatibilidade = {
        "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
        "O+": ["O+", "A+", "B+", "AB+"],
        "A-": ["A-", "A+", "AB-", "AB+"],
        "A+": ["A+", "AB+"],
        "B-": ["B-", "B+", "AB-", "AB+"],
        "B+": ["B+", "AB+"],
        "AB-": ["AB-", "AB+"],
        "AB+": ["AB+"]
    }
    return tipo_receptor in compatibilidade.get(tipo_doador, [])

# Lista de tipos sanguíneos possíveis
tipos_sanguineos = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]

if __name__ == "__main__":
    # Dados do usuário 1
    nome1 = input("Nome do usuário 1: ").strip().title()
    idade1 = input("Idade: ")
    email1 = input("Email: ").strip()
    telefone1 = input("Telefone: ")
    genero1 = input("Gênero: ").strip().title()
    tipo_sangue1 = random.choice(tipos_sanguineos)
    doenca1 = random.choice([True, False])

    usuario_1 = Pessoa(nome1, idade1, email1, telefone1, genero1, tipo_sangue1, doenca1)

    # Dados do usuário 2
    nome2 = input("Nome do usuário 2: ").strip().title()
    idade2 = input("Idade: ")
    email2 = input("Email: ").strip()
    telefone2 = input("Telefone: ")
    genero2 = input("Gênero: ").strip().title()
    tipo_sangue2 = random.choice(tipos_sanguineos)
    doenca2 = random.choice([True, False])

    usuario_2 = Pessoa(nome2, idade2, email2, telefone2, genero2, tipo_sangue2, doenca2)

    print("\n--- Dados do Usuário 1 (Doador) ---")
    usuario_1.exibir_dados()

    print("--- Dados do Usuário 2 (Receptor) ---")
    usuario_2.exibir_dados()

    print("\n--- Verificação de doação de sangue ---")
    if not usuario_1.doenca_sanguinea:
        if pode_doar(usuario_1.tipo_sanguineo, usuario_2.tipo_sanguineo):
            print(f"{usuario_1.nome} PODE doar sangue para {usuario_2.nome}.")
        else:
            print(f"{usuario_1.nome} NÃO pode doar sangue para {usuario_2.nome} (tipo incompatível).")
    else:
        print(f"{usuario_1.nome} NÃO pode doar sangue para {usuario_2.nome} (doença no sangue detectada).")
