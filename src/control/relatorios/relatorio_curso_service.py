from ...domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
from ...domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina
from ...domain.strategies.curso_cr_aluno_disciplina import CursoCRAlunoDisciplina

class RelatorioCursoService:
    """
    Serviço focado na geração de relatórios por Curso
    """
    def __init__(self, cursos, matriculas):
        self.cursos = cursos
        self.matriculas = matriculas
        

    def _executar_estrategia(self, codigo_curso, strategy, ano=None, semestre=None): 
        """
        Executa a estratégia desejada no objeto Curso fornecido.
        """
        if codigo_curso not in self.cursos:
            return 0.0
        curso = self.cursos[codigo_curso]
        curso.strategy = strategy
        return curso.media_cr(ano=ano, semestre=semestre)

    def media_cr_por_aluno(self, codigo_curso, ano=None, semestre=None):
        strategy = CursoCRPorAluno() 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre) 

    def media_cr_por_disciplina(self, codigo_curso, ano=None, semestre=None): 
        strategy = CursoCRPorDisciplina(self.matriculas) 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre)
    
    def media_cr_por_aluno_disciplina(self, codigo_curso, ano=None, semestre=None):
        strategy = CursoCRAlunoDisciplina(self.matriculas) 
        return self._executar_estrategia(codigo_curso, strategy, ano, semestre)

    def get_cr_agregado(self, ano=None, semestre=None, estrategia='disciplina'):
        """
        Retorna um dicionário com o CR agregado de cada curso: {curso_codigo: media_CR} e printa esses valores
        """
        print("\n----- Média de CR dos cursos ------")

        cr_cursos = {}
        
        # 1. Define qual estrategia de cálculo usar
        if estrategia == 'disciplina':
            calculo_metodo = self.media_cr_por_disciplina
            
        elif estrategia == 'aluno':
            calculo_metodo = self.media_cr_por_aluno
        
        elif estrategia == 'aluno_disciplina':
            calculo_metodo = self.media_cr_por_aluno_disciplina
        else:
            # Caso a estratégia não seja reconhecida
            calculo_metodo = self.media_cr_por_disciplina 

        # 2. Faz o cálculo para todos os cursos
        for codigo_curso in self.cursos.keys():
            media_cr = calculo_metodo(codigo_curso, ano, semestre)
            
            # 3. Adiciona ao dicionário de resultados
            cr_cursos[codigo_curso] = media_cr
            print(f"{codigo_curso} - {media_cr:.2f}")
            
        print("-----------------------------------")  
        return cr_cursos