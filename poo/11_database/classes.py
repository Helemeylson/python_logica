from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str
    telefone: str
    profissao: str
    peso: float
    altura: float

    def __str__(self):
        return f"olá, meu nome é {self.nome}"
    
    def __len__(self):
        return self.idade
    
    def __del__(self):
        print(f"objeto {self.nome} destruido com sucesso.")