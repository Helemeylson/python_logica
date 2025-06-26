import classes
import os


if __name__ == "__main__":
    usuario = classes.PessoaFisica("", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")
    while True:
        menu = input("\n1- Inserir dados do usuario.\n2- Inserir dados da empresa.\n3- Exibir dados\n4- Sair do programa.\n")
        match menu:
            case "1":
                try:
                    usuario.nome = input("Digite o nome do usuario: ").title().strip()
                    usuario.cpf = input("Digite o CPF do usuario: ").strip()
                    usuario.profissao = input("Digite a profissão do usuario: ").strip()
                    usuario.email = input("Digite o E-mail do usuario: ").lower().strip()
                    usuario.endereco = input("Digite o endereço do usuario: ").strip().title()
                    usuario.telefone = input("Digite o telefone do usuario: ").strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    continue

                except Exception as e:
                    print(f"Não foi possivel cadastrar dados do usuario: {e}")

            case "2":
                try:
                    empresa.razao_social = input("Digite a razão social da empresa: ").strip().title()
                    empresa.nome_fantasia = input("Digite o nome fantasia da empresa: ").strip().title()
                    empresa.cnpj = input("Digite o CNPJ da empresa: ").strip()
                    empresa.email = input("Digite o E-mail da empresa: ").lower().strip()
                    empresa.endereco = input("Digite o endereço da empresa: ").strip().lower()
                    empresa.telefone = input("Digite o telefone da empresa: ").strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                    
                except Exception as e:
                    print(f"Não foi possivel cadastrar os dados da empresa. {e}")

            case "3":
                try:
                    opcao = input("Digite:\n 1- para exibir dados do usuario \nou\n 2- para exibir dados da empresa.\n")
                    os.system("cls" if os.name == "nt" else "clear")

                    if opcao == "1":
                        usuario.exibir_dados()
                        continue
                    elif opcao == "2":
                        empresa.exibir_dados()
                        continue
                    else:
                        print("Opção invalida")

                except Exception as e:
                    print(f"Não foi possivel exibir dados. {e}")

            case "4":
                print("Encerrando o programa...")
                break

            case _:
                print("Entrada invalida apenas numeros de 1 a 3.")

        