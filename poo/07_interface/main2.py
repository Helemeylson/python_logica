import classes
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ").title().strip()
    cpf = input("Informe o CPF do usuário: ").strip()
    profissao = input("Informe a profissão do usuário: ").title().strip()
    email = input("Informe o e-mail do usuário: ").strip()
    endereco = input("Informe o endereço do usuário: ").title().strip()
    telefone = input("Informe o telefone do usuário: ").strip()

    return classes.PessoaFisica(nome, cpf, profissao, email, endereco, telefone)

def cadastrar_empresa():
    razao_social = input("Informe a razão social: ").strip().title()
    nome_fantasia = input("Informe o nome fantasia: ").strip().title()
    cnpj = input("Informe o CNPJ da empresa: ").strip()
    email = input("Informe o e-mail da empresa: ").strip()
    endereco = input("Informe o endereço da empresa: ").title().strip()
    telefone = input("Informe o telefone da empresa: ").strip()

    return classes.PessoaJuridica(razao_social, nome_fantasia, cnpj, email, endereco, telefone)

if __name__ == "__main__":
    usuario = None
    empresa = None

    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da empresa")
        print("3 - Exibir dados")
        print("4 - Sair do programa")

        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()

        match opcao:
            case "1":
                try:
                    usuario = cadastrar_usuario()
                    print("✅ Usuário cadastrado com sucesso!")
                except Exception as e:
                    print(f"❌ Erro ao cadastrar usuário: {e}")
                input("\nPressione Enter para continuar...")
                limpar_tela()

            case "2":
                try:
                    empresa = cadastrar_empresa()
                    print("✅ Empresa cadastrada com sucesso!")
                except Exception as e:
                    print(f"❌ Erro ao cadastrar empresa: {e}")
                input("\nPressione Enter para continuar...")
                limpar_tela()

            case "3":
                try:
                    print(f"\n{'='*10} DADOS DO USUÁRIO {'='*10}")
                    if usuario:
                        usuario.exibir_dados()
                    else:
                        print("Usuário ainda não cadastrado.")
                    
                    print(f"\n{'='*10} DADOS DA EMPRESA {'='*10}")
                    if empresa:
                        empresa.exibir_dados()
                    else:
                        print("Empresa ainda não cadastrada.")
                except Exception as e:
                    print(f"❌ Erro ao exibir dados: {e}")
                input("\nPressione Enter para continuar...")
                limpar_tela()

            case "4":
                print("Programa encerrado com sucesso.")
                break

            case _:
                print("❌ Opção inválida.")
                input("\nPressione Enter para continuar...")
                limpar_tela()
