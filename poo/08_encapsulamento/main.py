from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name== "nt" else "clear")

if __name__=="__main__":
    usuario = PessoaFisica(nome="", cpf="",profissao="", email="",telefone="" )
    empresa = PessoaJuridica(razao_social="", nome_fantasia="",cnpj="", email="",telefone="" )

    print(f"{'-'*20}Dados do usuario{'-'*20}")

    usuario.nome = input("informe o nome: ").title().strip()
    usuario.cpf = input("informe o cpf: ").title().strip()
    usuario.profissao = input("informe a profissão: ").title().strip()
    usuario.email = input("informe o email: ").title().strip()
    usuario.telefone = input("informe o telefone: ").title().strip()
   
    limpar()
    print(f"{'-'*20}Dados da empresa{'-'*20}")

    empresa.razao_social = input("informe o razao_social: ").title().strip()
    empresa.nome_fantasia = input("informe o nome_fantasia: ").title().strip()
    empresa.cnpj = input("informe o cnpj: ").title().strip()
    empresa.email = input("informe o email: ").title().strip()
    empresa.telefone = input("informe o telefone: ").title().strip()

    limpar()
    print(f"{'-'*20}Dados do usuario{'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"cpf: {usuario.cpf}")
    print(f"profissao: {usuario.profissao}")
    print(f"email: {usuario.email}")
    print(f"telefone: {usuario.telefone}")

    print(f"{'-'*20}Dados da empresa{'-'*20}")
    print(f"razao_social: {empresa.razao_social}")
    print(f"nome da empresa: {empresa.nome_fantasia}")
    print(f"profissao: {empresa.cnpj}")
    print(f"email: {empresa.email}")
    print(f"telefone: {empresa.telefone}")