from classes import Aluno, Curso
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0

    limpar()
    while True:
        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}\n")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar curso")
        print("3 - Matricular aluno no curso")
        print("4 - Listar cursos")
        print("5 - Listar alunos")
        print("6 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()

        limpar()

        match opcao:
            case "1":
                try:
                    nome = input("Informe o nome do aluno: ").strip().title()
                    cpf = input("Informe o CPF do aluno: ").strip()
                    matricula += 1
                    aluno = Aluno(nome, matricula, cpf)
                    alunos.append(aluno)
                    print(f"Aluno {aluno.nome} matriculado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar aluno. Erro: {e}")
                finally:
                    continue

            case "2":
                try:
                    nome_curso = input("Informe o nome do curso: ").strip().title()
                    curso = Curso(nome_curso)
                    cursos.append(curso)
                    print(f"Curso {curso.nome_curso} cadastrado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível cadastrar curso. Erro: {e}")
                finally:
                    continue

            case "3":
                try:
                    print(f"{'-'*10} Lista de alunos {'-'*10}")
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                        print('-'*40)

                    inscricao = int(input("Informe a matrícula do aluno: "))
                    aluno_encontrado = next((a for a in alunos if a.matricula == inscricao), None)

                    if aluno_encontrado:
                        print(f"{'-'*10} Lista de cursos {'-'*10}")
                        for curso in cursos:
                            print(f"Curso: {curso.nome_curso}")
                        nome_curso = input("Informe o curso desejado: ").strip().title()

                        curso_obj = next((c for c in cursos if c.nome_curso == nome_curso), None)
                        if curso_obj:
                            aluno_encontrado.inscrever_curso(curso_obj)
                            print(f"Aluno {aluno_encontrado.nome} inscrito no curso {curso_obj.nome_curso} com sucesso.")
                        else:
                            print("Curso não encontrado.")
                    else:
                        print("Aluno não encontrado.")
                except Exception as e:
                    print(f"Não foi possível matricular aluno. Erro: {e}")
                finally:
                    continue

            case "4":
                if not cursos:
                    print("Nenhum curso cadastrado.")
                else:
                    cursos.sort(key=lambda c: c.nome_curso)
                    for curso in cursos:
                        print(f"Curso: {curso.nome_curso}")
                        print("Alunos:")
                        alunos_do_curso = sorted(curso.listar_alunos())
                        for nome in alunos_do_curso:
                            print(f"- {nome}")
                        print('-'*40)

            case "5":
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                else:
                    alunos.sort(key=lambda a: a.nome)
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                        print("Cursos matriculados:")
                        for curso in aluno.listar_cursos():
                            print(f"- {curso}")
                        print('-'*40)

            case "6":
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida. Tente novamente.")
                continue
