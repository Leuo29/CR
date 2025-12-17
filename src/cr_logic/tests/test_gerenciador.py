import pytest
from cr_logic.control.gerenciador_entidades import GerenciadorEntidades

def test_processamento_completo_de_linhas():
    gerenciador = GerenciadorEntidades()
    dados_exemplo = [
        {
            'MATRICULA': '100',
            'COD_CURSO': '10',
            'COD_DISCIPLINA': 'D1',
            'CARGA_HORARIA': '40',
            'NOTA': '80',
            'ANO_SEMESTRE': '20231'
        },
        {
            'MATRICULA': '100',
            'COD_CURSO': '10',
            'COD_DISCIPLINA': 'D2',
            'CARGA_HORARIA': '20',
            'NOTA': '100',
            'ANO_SEMESTRE': '20231'
        }
    ]
    
    
    gerenciador.processar_linhas(dados_exemplo)
    
    
    matriculas = gerenciador.get_matriculas()
    aluno_100 = next(m for m in matriculas if m.codigo == '100')
    
    
    assert aluno_100.cr == pytest.approx(86.67, rel=1e-2)