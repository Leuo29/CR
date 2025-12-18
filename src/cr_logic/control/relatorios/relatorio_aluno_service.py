class RelatorioAlunoService:
    """
    gera de relatórios individuais de Aluno/Matricula.
    """
    def __init__(self, matriculas):
        self.matriculas = matriculas
        

    def get_cr_individual(self):
        """
        retorna um dicionário com o CR de cada matrícula e printa os valores
        """
        print("\n------- O CR dos alunos é: --------")
        cr_alunos = {}
        for matricula in self.matriculas:
            cr_alunos[str(matricula.codigo)] = matricula.cr
            print(f"{matricula.codigo} - {matricula.cr:.2f}")
        print("-----------------------------------")
        return cr_alunos