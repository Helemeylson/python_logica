from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        email="",
        telefone="",
        profissao="",
        peso=0.0,
        altura=0.0
    )

    
    usuario.nome = "Fulano"
    usuario.idade = 18
    usuario.email = "fulano@gmail.com"
    usuario.telefone = "(61) 99235-2425"
    usuario.profissao = "Programador"
    usuario.peso = 100
    usuario.altura = 1.85

'''   
print(f"Nome: {usuario.nome}")
print(f"Idade: {usuario.idade}")
print(f"E-mail: {usuario.email}")
print(f"Telefone: {usuario.telefone}")
print(f"Profissão: {usuario.profissao}")
print(f"Peso: {usuario.peso}")
print(f"Altura: {usuario.altura}")'''

print(f'''f{usuario}, tenho {len(usuario)} anos. Segue meus dados:")
Nome: {usuario.nome}
Idade: {usuario.idade}
E-mail: {usuario.email}
Telefone: {usuario.telefone}
Profissão: {usuario.profissao}
Peso: {usuario.peso}
Altura: {usuario.altura}''')
print(usuario)
del(usuario)

