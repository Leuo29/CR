from ...domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
from ...domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina
from ...domain.strategies.curso_cr_aluno_disciplina import CursoCRAlunoDisciplina


class RelatorioCursoService:
    """
    responsável por calcular e agrupar
    os resultados de CR por curso.
    """

    def __init__(self, cursos, matriculas):
        self.cursos = cursos
        self.matriculas = matriculas
        

    def _executar_estrategia(self, codigo_curso, strategy, ano=None, semestre=None): 
        """aplica a estratégia ao curso """
        if codigo_curso not in self.cursos:
            return 0.0

        curso = self.cursos[codigo_curso]
        curso.strategy = strategy

        return curso.media_cr(ano=ano, semestre=semestre)


    def media_cr_por_aluno(self, codigo_curso, ano=None, semestre=None):
        """calcula o CR do curso pela média simples dos CRs dos alunos do curso"""
        strategy = CursoCRPorAluno() 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre) 


    def media_cr_por_disciplina(self, codigo_curso, ano=None, semestre=None): 
        """calcula o CR do curso pela média das disciplinas"""
        strategy = CursoCRPorDisciplina(self.matriculas) 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre)
    

    def media_cr_por_aluno_disciplina(self, codigo_curso, ano=None, semestre=None):
        """
        calcula o CR do curso 
        usando os alunos que cursaram ao menos uma disciplina do curso
        """
        strategy = CursoCRAlunoDisciplina(self.matriculas) 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre)


    def get_cr_agregado(self, ano=None, semestre=None, estrategia='disciplina'):
        """
        retorna um dicionário com o CR de cada curso e printa
        """
        print("\n----- Média de CR dos cursos ------")
        cr_cursos = {}
        
        # define qual método de cálculo será usado
        if estrategia == 'disciplina':
            calculo_metodo = self.media_cr_por_disciplina
            
        elif estrategia == 'aluno':
            calculo_metodo = self.media_cr_por_aluno
        
        elif estrategia == 'aluno_disciplina':
            calculo_metodo = self.media_cr_por_aluno_disciplina
        else:
            # caso nenhum seja definido
            calculo_metodo = self.media_cr_por_disciplina 

        # executa o cálculo para todos os cursos
        for codigo_curso in self.cursos.keys():
            media_cr = calculo_metodo(codigo_curso, ano, semestre)
            cr_cursos[codigo_curso] = media_cr
            print(f"{codigo_curso} - {media_cr:.2f}")
        print("-----------------------------------")    
        return cr_cursos
