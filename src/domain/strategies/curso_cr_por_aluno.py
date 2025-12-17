from .curso_cr_strategy import CursoCRStrategy

class CursoCRPorAluno(CursoCRStrategy):
    """
    Calcula a média de todos os CRs dos alunos daquele curso em específico.
    """
    
    def calcular_media(self, curso, ano=None, semestre=None):
        
        total_cr = 0
        qtd = 0
        
        
        for matricula in curso.matriculas:
            
            
            if matricula.cr > 0:
                total_cr += matricula.cr
                qtd += 1

        if qtd > 0:
            return total_cr / qtd 
        else:
            return 0.0