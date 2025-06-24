import random

class Pessoa:
        def __init__(self, nome, email, profissao, humor):


            self.nome = nome
            self.email = email
            self.profissao = profissao
            self.humor = humor


        def dar_boas_vindas(self):
            return "Olá, boa tarde!"
        
        def cumprimentar(self):
            return f"Olá, eu me chamo {self.nome}. É um Prazer!"
        
        def perguntar(self):
            return f"Qual o seu nome?"
        
        def cartao_de_visitas(self):
            print(f"Nome: {self.nome}")
            print(f"Nome: {self.email}")
            print(f"Nome: {self.profissao}")
        def ofender(self):
             return f"Quem liga? Me erra! Vai ver se não estou na esquina!"


if __name__== "__main__":
     usuario_masculino = Pessoa("","","",bool(random.getrandbits(1)))
     usuario_feminino = Pessoa("","","",bool(random.getrandbits(1)))


     usuario_masculino.nome = input("informe seu nome: ").strip().title()
     usuario_masculino.email = input("informe seu e-mail: ").strip().title()
     usuario_masculino.profissao = input("informe sua profissao: ").strip().title()
     
     
     usuario_feminino.nome = input("informe seu nome: ").strip().title()
     usuario_feminino.email = input("informe seu e-mail: ").strip().title()
     usuario_feminino.profissao = input("informe sua profissao: ").strip().title()

     print(f"homem: -{usuario_masculino.dar_boas_vindas()}")
     print(f"Mulher: -{usuario_feminino.dar_boas_vindas()}")
     print(f"homem: -{usuario_masculino.perguntar()}")
     if usuario_feminino.humor is True:
          print(f"Mulher: ={usuario_feminino.cumprimentar()}")
          print(f"Mulher: -{usuario_feminino.perguntar()}")
          usuario_masculino.humor = usuario_feminino.humor
          print(f"homem: -{usuario_masculino.cumprimentar()}")
          print(f"homem: Bom humor = {usuario_masculino.humor}")
          print("segue meu cartao de visitas:")
          print(usuario_masculino.cartao_de_visitas())
                
     else:
          print(f"Mulher: - {usuario_feminino.ofender()}")
          usuario_masculino.humor = usuario_feminino.humor
          print(f"Homem: Bom humor = {usuario_masculino.humor} ")



