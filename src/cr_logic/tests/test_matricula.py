import pytest
from cr_logic.domain.matricula import Matricula
from cr_logic.domain.curso import Curso
from cr_logic.domain.disciplina import Disciplina
from cr_logic.domain.nota import Nota

def test_deve_calcular_cr_ponderado_corretamente():
    
    curso = Curso("10")
    matricula = Matricula("100", curso)
    
    # Disciplina A: Nota 10, Carga 2h
    d1 = Disciplina("D1", "Disc 1", 2, 2023, 1)
    # Disciplina B: Nota 5, Carga 4h
    d2 = Disciplina("D2", "Disc 2", 4, 2023, 1)
    
    matricula.adicionar_nota(Nota(d1, 10.0))
    matricula.adicionar_nota(Nota(d2, 5.0))
    
    
    # Cálculo esperado: ((10 * 2) + (5 * 4)) / (2 + 4) = 40 / 6 = 6.666...
    cr = matricula.calcular_cr()
    
    
    assert cr == pytest.approx(6.67, rel=1e-2)

def test_cr_deve_ser_zero_quando_nao_ha_notas():
    curso = Curso("10")
    matricula = Matricula("101", curso)
    assert matricula.calcular_cr() == 0.0

def test_carga_horaria_negativa_deve_ser_tratada_como_zero():
    d = Disciplina("DX", "Erro", -10, 2023, 1)
    assert d.carga_horaria == 0