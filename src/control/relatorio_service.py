from ..domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
from ..domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina


class RelatorioService:

    def __init__(self, cursos, matriculas):
        self.cursos = cursos
        self.matriculas = matriculas

   
    def _executar_estrategia(self, codigo_curso, strategy, ano=None, semestre=None):

        if codigo_curso not in self.cursos:
            return 0.0
        
        curso = self.cursos[codigo_curso]
        
        curso.strategy = strategy
        
  
        return curso.media_cr(ano, semestre) 

  
    def media_cr_por_aluno(self, codigo_curso):
        strategy = CursoCRPorAluno() 

        return self._executar_estrategia(codigo_curso, strategy)

    def media_cr_por_disciplina(self, codigo_curso):
        strategy = CursoCRPorDisciplina(self.matriculas) 

        return self._executar_estrategia(codigo_curso, strategy)
    

    def media_cr_por_disciplina_filtrado(self, codigo_curso, ano=None, semestre=None):
        """Calcula a média de CR agrupada por disciplina, filtrada por ano e/ou semestre."""
        strategy = CursoCRPorDisciplina(self.matriculas) 

        return self._executar_estrategia(codigo_curso, strategy, ano, semestre)