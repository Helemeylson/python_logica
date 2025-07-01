from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="", profissao="", genero="", email="",telefone="", endereco="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", website="", email="", telefone="", endereco="")

    limpar()
    print(f"{'-'*20} Dados do usuário{'-'*20} ")
    usuario.nome = input("informe o nome do usuario: ").strip().title()
    usuario.profissao = input("informe o profissao do usuario: ").strip().title()
    usuario.genero = input("informe o genero do usuario: ").strip().title()
    usuario.email = input("informe o email do usuario: ").strip().title()
    usuario.telefone = input("informe o telefone do usuario: ").strip().title()
    usuario.endereco = input("informe o endereco do usuario: ").strip().title()
    
 
    print(f"{'-'*20} Dados da empresa{'-'*20} ")
    empresa.nome_fantasia = input("informe o nome_fantasia do empresa: ").strip().title()
    empresa.cnpj = input("informe o cnpj do empresa: ").strip().title()
    empresa.website = input("informe o website do empresa: ").strip().title()
    empresa.email = input("informe o email do empresa: ").strip().title()
    empresa.telefone = input("informe o telefone do empresa: ").strip().title()
    empresa.endereco = input("informe o endereco do empresa: ").strip().title()

    limpar()


    print(f"{usuario}.segue meus dados")
    usuario.exibir_dados()
    print(f"{empresa}.Segue os dados da empresa:")
    empresa.exibir_dados()


    del(usuario)
    del(empresa)