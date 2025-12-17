from ..domain.curso import Curso
from ..domain.disciplina import Disciplina
from ..domain.matricula import Matricula
from ..domain.nota import Nota

class GerenciadorEntidades:
    def __init__(self):
        self.cursos = {}
        self.disciplinas_base = {}
        self.alunos_matriculas = {}
        

    def processar_linhas(self, dados):
        """
        Processa uma lista de linhas de dados e cria os objetos de domínio.
        """
        for linha in dados:
            self._processar_linha(linha)
            
        # Calcular o CR para todas as matrículas após o processamento
        for matricula in self.alunos_matriculas.values():
            matricula.calcular_cr()

    def _processar_linha(self, linha):
        """
        Processa uma linha de dados para criar ou atualizar as entidades.
        """
        
        # 1. Extração de dados
        ano_semestre_str = str(linha.get('ANO_SEMESTRE', '00000'))
        ano = int(ano_semestre_str[:4])
        semestre = int(ano_semestre_str[4])
        codigo_curso = str(linha['COD_CURSO'])
        codigo_disciplina = linha['COD_DISCIPLINA']
        carga_horaria = int(linha['CARGA_HORARIA'])
        matricula_aluno_id = str(linha['MATRICULA'])
        nota_valor = float(linha['NOTA'])


        # 2. Gerenciar Curso
        if codigo_curso not in self.cursos:
            self.cursos[codigo_curso] = Curso(codigo_curso)
            self.cursos[codigo_curso].strategy = None
        curso = self.cursos[codigo_curso]

        # 3. Gerenciar Disciplina Base 
        if codigo_disciplina not in self.disciplinas_base:
            self.disciplinas_base[codigo_disciplina] = Disciplina(
                codigo_disciplina, codigo_disciplina, carga_horaria, ano, semestre, None
            )
        disciplina_base = self.disciplinas_base[codigo_disciplina]

        # 4. Gerenciar Matrícula do Aluno
        if matricula_aluno_id not in self.alunos_matriculas:
            student_matricula = Matricula(matricula_aluno_id, curso)
            self.alunos_matriculas[matricula_aluno_id] = student_matricula
            curso.adicionar_matricula(student_matricula)
        student_matricula = self.alunos_matriculas[matricula_aluno_id]

        # 5. Criar Disciplina para a Nota
        disciplina_para_nota = Disciplina(
            disciplina_base.codigo,
            disciplina_base.nome,
            disciplina_base.carga_horaria,
            ano,
            semestre,
            curso
        )

        # 6. Criar e Adicionar Nota
        nota = Nota(disciplina_para_nota, nota_valor)
        student_matricula.adicionar_nota(nota)

    def get_cursos(self):
        return self.cursos

    def get_matriculas(self):
        return list(self.alunos_matriculas.values())

    def get_disciplinas_base(self):
        return self.disciplinas_base