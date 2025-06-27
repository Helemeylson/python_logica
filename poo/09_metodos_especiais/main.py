from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name=="nt" else "clear")

if __name__=="__main__":
    usuario = Pessoa(nome="", profissao="", idade="")
    while True:
        print('''1- inserir dados e exibir
2- Sair do programa''')
        opcao = input("informe a opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":    
             try:
                usuario.nome = input("informe o nome: ").strip().title()
                usuario.idade = int(input("informe o idade: "))
                usuario.profissao = input("informe a profissao: ").strip()

                limpar()
                print(usuario)
                print(f"idade de {usuario.nome}: {len(usuario)} anos")
             except Exception as e:
                print(f"não foi possivel executar o programa; {e}")
                break
            case "2":
              print("encerrando...")
              break
            case _:
              print("opção inválida.")
              continue
      

  
 