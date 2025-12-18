import pytest
from cr_logic.domain.curso import Curso
from cr_logic.domain.matricula import Matricula
from cr_logic.domain.disciplina import Disciplina
from cr_logic.domain.nota import Nota
from cr_logic.domain.strategies.curso_cr_por_disciplina import CursoCRPorDisciplina
from cr_logic.domain.strategies.curso_cr_por_aluno import CursoCRPorAluno
from cr_logic.domain.strategies.curso_cr_aluno_disciplina import CursoCRAlunoDisciplina

@pytest.fixture
def cenario_complexo():
    """
    Cria dois alunos e disciplinas dentro e fora do curso,
    para testar os diferentes critérios de cálculo de CR do curso.
    """
    curso_cc = Curso("CC")
    curso_ext = Curso("EXT")
    
    # Disciplinas
    d1 = Disciplina("D1", "Prog1", 40, 2023, 1, curso_cc)
    d2 = Disciplina("D2", "Lab1", 20, 2023, 1, curso_cc)
    d_fora = Disciplina("DX", "Extra", 100, 2023, 1, curso_ext)
    
    # Aluno A
    m_a = Matricula("A", curso_cc)
    m_a.adicionar_nota(Nota(d1, 100)) 
    m_a.adicionar_nota(Nota(d_fora, 100)) 
    m_a.calcular_cr() # CR Global = 100.0
    
    # Aluno B
    m_b = Matricula("B", curso_cc)
    m_b.adicionar_nota(Nota(d1, 50)) 
    m_b.adicionar_nota(Nota(d2, 80)) 
    m_b.calcular_cr() # CR Global = 60.0
    
    curso_cc.adicionar_matricula(m_a)
    curso_cc.adicionar_matricula(m_b)
    
    return curso_cc, [m_a, m_b]

def test_strategy_por_aluno(cenario_complexo):
    """Média simples dos CRs dos alunos vinculados ao curso"""
    curso, _ = cenario_complexo
    strategy = CursoCRPorAluno()
    # (100.0 + 60.0) / 2 = 80.0
    assert strategy.calcular_media(curso) == pytest.approx(80.0)

def test_strategy_por_disciplina(cenario_complexo):
    """Média ponderada apenas das notas de disciplinas do curso"""
    curso, todas_matriculas = cenario_complexo
    strategy = CursoCRPorDisciplina(todas_matriculas)
    # aluno A (no curso): 100 * 40 = 4000
    # aluno B (no curso): 50*40 + 80*20 = 3600
    # (4000 + 3600) / (40 + 60) = 7600 / 100 = 76.0
    assert strategy.calcular_media(curso) == pytest.approx(76.0)

def test_strategy_aluno_disciplina(cenario_complexo):
    """Média do CR global de alunos que passaram pelo curso"""
    curso, todas_matriculas = cenario_complexo
    strategy = CursoCRAlunoDisciplina(todas_matriculas)
    # Ambos cursaram disciplinas de CC, então usamos todos os crs ja calculados:
    # (100.0 + 60.0) / 2 = 80.0
    assert strategy.calcular_media(curso) == pytest.approx(80.0)
