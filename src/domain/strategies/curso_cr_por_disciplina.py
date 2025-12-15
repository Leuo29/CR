from .curso_cr_strategy import CursoCRStrategy

class CursoCRPorDisciplina(CursoCRStrategy):
    # CORREÇÃO DEFINITIVA: Aceita a injeção da lista completa de Matrículas
    def __init__(self, todas_as_matriculas):
        self.todas_as_matriculas = todas_as_matriculas

    def calcular_media(self, curso):
        total_ponderado = 0
        total_carga = 0

        # CORREÇÃO: Itera sobre TODAS as matrículas injetadas para não perder notas.
        for matricula in self.todas_as_matriculas:
            for nota in matricula.notas:
                # O filtro funciona perfeitamente, pois a nota está ligada à referência de Curso correta.
                if nota.disciplina.curso is not None and nota.disciplina.curso.nome == curso.nome:
                    total_ponderado += nota.valor * nota.disciplina.carga_horaria
                    total_carga += nota.disciplina.carga_horaria

        return (total_ponderado / total_carga) if total_carga > 0 else 0.0