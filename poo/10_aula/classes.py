class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_inscritos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            if self not in curso.alunos_inscritos:
                curso.adicionar_aluno(self)

    def listar_cursos(self):
        return [curso.nome_curso for curso in self.cursos_inscritos]

    def __del__(self):
        print(f"Objeto Aluno '{self.nome}' deletado com sucesso!")


class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_inscritos = []

    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            if self not in aluno.cursos_inscritos:
                aluno.inscrever_curso(self)

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos_inscritos]

    def __del__(self):
        print(f"Objeto Curso '{self.nome_curso}' deletado com sucesso!")
