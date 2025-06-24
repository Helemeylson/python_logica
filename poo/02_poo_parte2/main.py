class Pessoa:
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade}, trabalho como {self.profissao} e meu email é {self.email}")
if __name__=="__main__":

    usuario = Pessoa()

    usuario.apresentar()