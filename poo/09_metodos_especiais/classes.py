class Pessoa:
    def __init__(self, nome, profissao,idade):
        self.nome = nome
        self.profissao = profissao
        self.idade = idade

    def __len__(self):
         return self.idade


    def __str__(self):
            return f"olá, meu nome é {self.nome}, tenho {len(self)} e trabalho com {self.profissao}."
    
    def __del__(self):
        print (f"Objeto identificado por {self.nome} foi destruído com sucesso!")
    
    