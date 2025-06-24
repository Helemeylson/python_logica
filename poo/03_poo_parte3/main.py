class Pessoa:

    def __init__(self, nome, idade, email, profissao):

        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    def apresentar(self):  
        print(f"ola, meu nome é {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao}, meu e-mail é {self.email}.")

if __name__ == "__main__":
    usuario = Pessoa("",0,"","")

    try:
        usuario.nome = input("informe o nome do usuário: ").title().strip()
        usuario.idade = input("informe a idade do usuário: ").title().strip()
        usuario.email = input("informe o email do usuário: ").title().strip()
        usuario.profissao = input("informe a profissão do usuário: ").title().strip()

        usuario.apresentar()

    except Exception as e:
        print(f"Não foi possivel executar o programa. {e}.")
        
