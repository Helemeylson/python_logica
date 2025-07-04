#  TODO - atividade 10: crie um programa que exiba um menu com as seguintes operações:
# - Cadastrar um novo usuário no banco
# - Listar todos os usuários do banco
# - Sair do programa
# # NOTE - a entidade deverá ser gerada pelo python
# # NOTE - nome do banco: db_atividade_10. Entidade Usuario.

# Atributos:
# - Nome
# - CPF
# - E-mail
# - Data de Nascimento
# - Telefone
# - Profissão
# - Endereço
# - Altura
# - Peso
#considere que em atributos deve existir um id para chave primária.

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import sys

# Conexão com o banco
engine = create_engine("sqlite:///db_atividade_10.db")
Base = declarative_base()

# Entidade Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    email = Column(String)
    data_nascimento = Column(Date)
    telefone = Column(String)
    profissao = Column(String)
    endereco = Column(String)
    altura = Column(Float)
    peso = Column(Float)

# Criar as tabelas
Base.metadata.create_all(engine)

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Função para cadastrar usuário
def cadastrar_usuario():
    print("\n📝 Cadastro de novo usuário:")
    try:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        data_str = input("Data de nascimento (dd/mm/aaaa): ")
        data_nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()
        telefone = input("Telefone: ")
        profissao = input("Profissão: ")
        endereco = input("Endereço: ")
        altura = float(input("Altura (em metros): "))
        peso = float(input("Peso (em kg): "))

        novo_usuario = Usuario(
            nome=nome,
            cpf=cpf,
            email=email,
            data_nascimento=data_nascimento,
            telefone=telefone,
            profissao=profissao,
            endereco=endereco,
            altura=altura,
            peso=peso
        )

        session.add(novo_usuario)
        session.commit()
        print("✅ Usuário cadastrado com sucesso!\n")

    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao cadastrar: {e}\n")

# Função para listar usuários
def listar_usuarios():
    print("\n📋 Lista de usuários:")
    usuarios = session.query(Usuario).all()
    if not usuarios:
        print("Nenhum usuário encontrado.")
    else:
        for u in usuarios:
            print(f"\nID: {u.id}\nNome: {u.nome}\nCPF: {u.cpf}\nEmail: {u.email}")
            print(f"Data Nascimento: {u.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"Telefone: {u.telefone}\nProfissão: {u.profissao}")
            print(f"Endereço: {u.endereco}\nAltura: {u.altura} m\nPeso: {u.peso} kg\n")

# Menu principal
def menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Cadastrar um novo usuário")
        print("2. Listar todos os usuários")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            print("👋 Saindo do programa. Até mais!")
# Executar o menu
if __name__ == "__main__":
    menu()

