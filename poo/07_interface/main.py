import classes
import os

if __name__ == "__main__":
   usuario = classes.PessoaFisica("","","","","","")
   empresa = classes.PessoaJuridica("","","","","","")



   while True:
        print("1 - inserir dados do usuario: ")
        print("2 - inserir dados da empresa: ")
        print("3 - exibir dados: ")
        print("4 - sair do programa: ")
        opcao = input("informe a opção desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                try:
                    usuario.nome = input("informe o nome do usuario: ").title().strip()
                    usuario.cpf = input("informe o cpf do usuario: ").title().strip()
                    usuario.profissao = input("informe a profissao do usuario: ").title().strip()
                    usuario.email = input("informe o email do usuario: ").title().strip()
                    usuario.endereco = input("informe o endereço do usuario: ").title().strip()
                    usuario.telefone = input("informe o telefone do usuario: ").title().strip()

                    os.system("cls" if os.name == "nt" else "clear")

                except Exception as e:
                    print(f"não foi possivel inserir os dados")
                finally:
                    continue
                
            case "2":
                try:
                    empresa.razao_social = input("informe a razao social").strip().title()
                    empresa.nome_fantasia = input("informe o nome fantasia").strip().title()
                    usuario.cnpj = input("informe o cnpj do empresa").title().strip()
                    usuario.email = input("informe o email do empresa").title().strip()
                    usuario.endereco = input("informe o endereco do empresa").title().strip()
                    usuario.telefone = input("informe o telefone do empresa").title().strip()
                except Exception as e:
                    print(f"não foi possível {e}")
                finally:
                    continue
            case "3":
                try:
                    print(f"{'-'*20}Dados do usuario{'-'*20}\n")
                    usuario.exibir_dados()
                    print(f"{'-'*20}DADOS DA EMPRESA{'-'*20}\n")
                    empresa.exibir_dados()
                except Exception as e:
                    print(f"Não foi possível exibir  os dados. {e}")
                finally:
                    continue

               
            case "4":
                print("programa encerrando...")
                break
            case _:
                print("opção inválida")
                continue
          
        

    