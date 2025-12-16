from .curso_cr_strategy import CursoCRStrategy

class CursoCRPorDisciplina(CursoCRStrategy):
    
    def __init__(self, todas_as_matriculas):
        self.todas_as_matriculas = todas_as_matriculas

    def calcular_media(self, curso, ano=None, semestre=None):
        total_ponderado = 0
        total_carga = 0

        
        for matricula in self.todas_as_matriculas:
            for nota in matricula.notas:
                
                if nota.disciplina.curso is not None and nota.disciplina.curso.nome == curso.nome:
                    
                    #Lógica de Filtragem por Ano e Semestre
                    deve_incluir = True
                    
                    # 1. Filtrar por ano, se 'ano' foi fornecido
                    if ano is not None:
                        # Assumindo que nota.disciplina.ano existe e tem o valor esperado
                        if nota.disciplina.ano != ano:
                            deve_incluir = False
                    # 2. Filtrar por semestre, SE 'semestre' foi fornecido E 'ano' também foi fornecido
                    if deve_incluir and semestre is not None and ano is not None:
                        if nota.disciplina.semestre != semestre:
                            deve_incluir = False
                            
                    # 3. Se passou pelos filtros, incluir no cálculo
                    if deve_incluir:
                        total_ponderado += nota.valor * nota.disciplina.carga_horaria
                        total_carga += nota.disciplina.carga_horaria

        return (total_ponderado / total_carga) if total_carga > 0 else 0.0