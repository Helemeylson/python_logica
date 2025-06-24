class Pessoa:
    
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

if __name__ == "__main__":
    usuario = Pessoa()

    print(f"Nome: {usuario.nome}.")
    print(f"Idade: {usuario.idade}.")
    print(f"E-mail: {usuario.email}.")
    print(f"Profissão: {usuario.profissao}.")

