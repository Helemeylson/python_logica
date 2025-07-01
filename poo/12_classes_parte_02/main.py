from classes import PessoaFisica, PessoaJuridica
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def separacao():
    print('-=-'*40)

if __name__ == "__main__":
    usuario = PessoaFisica(
        nome="", 
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereco="",
        )

    empresa = PessoaJuridica(
        razao_social="", 
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco="",
        )
    
    print("informe os dados do usuário:\n")
    usuario.nome = input("informe o nome do usuario: ").strip().title()
    usuario.cpf = input("informe o cpf do usuario: ").strip()
    usuario.profissao = input("informe a profissao do usuario: ").strip().title()
    usuario.email = input("informe o email do usuario: ").strip().title()
    usuario.telefone = input("informe a telefone do usuario: ").strip()
    usuario.endereco = input("informe o endereço do usuario: ").strip().title()

    limpar_tela()

    print("informe os dados da empresa:\n")
    empresa.razao_social = input("informe a razão social: ").strip().title()
    empresa.nome_fantasia = input("informe o nome fantasia da empresa: ").strip()
    empresa.cnpj = input("informe a cnpj da empresa: ").strip().title()
    empresa.email = input("informe o email da empresa: ").strip().title()
    empresa.telefone = input("informe a telefone da empresa: ").strip()
    empresa.endereco = input("informe o endereço da empresa: ").strip().title()
    
    limpar_tela()

    print(usuario)
    separacao()
    print(empresa)
    separacao()