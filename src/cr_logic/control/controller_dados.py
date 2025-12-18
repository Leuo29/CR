from ..domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
from ..domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina
from ..domain.strategies.curso_cr_aluno_disciplina import CursoCRAlunoDisciplina
from ..infra.leitor_csv import LeitorCSV

from .relatorios.relatorio_aluno_service import RelatorioAlunoService
from .relatorios.relatorio_curso_service import RelatorioCursoService
from .gerenciador_entidades import GerenciadorEntidades 


class ControllerDados:
    """
    -classe controller
    -Coordena a leitura do arquivo, a criação das entidades
    e geração dos relatório.
    """

    def __init__(self, file_object):
        # responsável pela leitura do arquivo CSV
        self.leitor = LeitorCSV(file_object)

        # cria o gerenciador q cria as entidades
        self.gerenciador_entidades = GerenciadorEntidades()
        
        self.cursos = {} 
        self.alunos_matriculas = {} 
        
        self.relatorio_aluno_service = None
        self.relatorio_curso_service = None
        

    def processar_dados(self):
        """
        executa:
        -leitura do CSV
        -criação das entidades
        -relatórios
        """
        dados = self.leitor.ler_dados()
        self.gerenciador_entidades.processar_linhas(dados)
        
        self.cursos = self.gerenciador_entidades.get_cursos()
        self.alunos_matriculas = self.gerenciador_entidades.get_matriculas()

        # inicializa os relatórios
        self.relatorio_aluno_service = RelatorioAlunoService(self.alunos_matriculas)
        self.relatorio_curso_service = RelatorioCursoService(
            self.cursos, 
            self.alunos_matriculas
        )
        

    def get_matriculas(self):
        """retorna todas as matrículas"""
        return self.alunos_matriculas

    def get_cursos(self):
        """retorna os cursos criados a partir do arquivo"""
        return self.cursos


    def get_cr_por_aluno_report(self):
        """
        gera o relatório de CR individual por aluno.
        """
        if not self.relatorio_aluno_service:
            return {}
        return self.relatorio_aluno_service.get_cr_individual()


    def get_cr_por_curso_report(self, ano=None, semestre=None, estrategia='disciplina'):
        """
        gera o relatório de CR por curso
        """
        if not self.relatorio_curso_service:
            return {}
            
        return self.relatorio_curso_service.get_cr_agregado(
            ano=ano,
            semestre=semestre,
            estrategia=estrategia 
        )
