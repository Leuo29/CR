from .curso_cr_strategy import CursoCRStrategy

class CursoCRPorAluno(CursoCRStrategy):
    def calcular_media(self, curso):
        total_cr = 0
        qtd = 0
        for matricula in curso.matriculas:
            total_cr += matricula.cr
            qtd += 1
        return total_cr / qtd if qtd > 0 else 0.0
