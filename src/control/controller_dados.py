from ..domain.curso import Curso
from ..domain.disciplina import Disciplina
from ..domain.matricula import Matricula
from ..domain.nota import Nota
from ..infra.leitor_csv import LeitorCSV


class ControllerDados:
    def __init__(self, arquivo_csv: str):
        self.leitor = LeitorCSV(arquivo_csv)
        self.cursos = {}
        
        self.disciplinas_base = {} 
        
        self.alunos_matriculas = {}

    def processar_dados(self):
        dados = self.leitor.ler_dados()  

        for linha in dados:
            
            codigo_curso = str(linha['COD_CURSO'])
            if codigo_curso not in self.cursos:
                self.cursos[codigo_curso] = Curso(codigo_curso)
                curso = self.cursos[codigo_curso]
                curso.strategy = None  
            curso = self.cursos[codigo_curso]

            
            codigo_disciplina = linha['COD_DISCIPLINA']
            carga_horaria = int(linha['CARGA_HORARIA'])
            
            if codigo_disciplina not in self.disciplinas_base:
                
                self.disciplinas_base[codigo_disciplina] = Disciplina(
                    codigo_disciplina, codigo_disciplina, carga_horaria, None
                )
            disciplina_base = self.disciplinas_base[codigo_disciplina]

            
            matricula_aluno_id = str(linha['MATRICULA'])
            if matricula_aluno_id not in self.alunos_matriculas:
                student_matricula = Matricula(matricula_aluno_id, curso)
                self.alunos_matriculas[matricula_aluno_id] = student_matricula
                curso.adicionar_matricula(student_matricula)
            student_matricula = self.alunos_matriculas[matricula_aluno_id]
            
             
            
 
            disciplina_para_nota = Disciplina(
                disciplina_base.codigo, 
                disciplina_base.nome, 
                disciplina_base.carga_horaria, 
                curso 
            )

         
            nota = Nota(disciplina_para_nota, float(linha['NOTA']))
            student_matricula.adicionar_nota(nota)

     
        for matricula in self.alunos_matriculas.values():
            matricula.calcular_cr()

    def get_matriculas(self):

        return list(self.alunos_matriculas.values())

    def get_cursos(self):

        return self.cursos


    def media_cr_por_aluno(self, codigo_curso):

        from ..domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
        if codigo_curso in self.cursos:
            curso = self.cursos[codigo_curso]
            curso.strategy = CursoCRPorAluno()
            return curso.media_cr()
        return 0.0

    def media_cr_por_disciplina(self, codigo_curso):

        from ..domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina
        if codigo_curso in self.cursos:
            curso = self.cursos[codigo_curso]

            curso.strategy = CursoCRPorDisciplina(list(self.alunos_matriculas.values()))
            return curso.media_cr()
        return 0.0
