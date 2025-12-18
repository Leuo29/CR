from .curso_cr_strategy import CursoCRStrategy

class CursoCRPorDisciplina(CursoCRStrategy):
    
    def __init__(self, todas_as_matriculas):
        # Pega todas as matrículas disponíveis
        self.todas_as_matriculas = todas_as_matriculas

    def calcular_media(self, curso, ano=None, semestre=None):

        """
        Calcula o CR ponderado pelas cargas horárias das disciplinas
        Retorna 0.0 se não houver notas
        somatorio( Notas * cargas)/somatorio(cargas) 
        """
        somatorio_nota_carga = 0
        somatorio_carga = 0
    
        
        for matricula in self.todas_as_matriculas:
            for nota in matricula.notas:
                # verifica se a disciplina pertence ao curso
                if nota.disciplina.curso is not None and nota.disciplina.curso.nome == curso.nome:
                    deve_incluir = True
                    # 1 Filtra por ano se tiver 
                    if ano is not None:
                        if str(nota.disciplina.ano) != ano:
                            deve_incluir = False
                            
                    # 2 Filtra por semestre se tiver
                    if deve_incluir and semestre is not None and ano is not None:
                        
                        if str(nota.disciplina.semestre) != semestre:
                            deve_incluir = False
                    # 3 Se passou pelos filtros, inclui na soma
                    if deve_incluir:
                        somatorio_nota_carga += nota.valor * nota.disciplina.carga_horaria
                        somatorio_carga += nota.disciplina.carga_horaria

        if somatorio_carga > 0:
            return (somatorio_nota_carga / somatorio_carga)
        else:
            return 0.0  # Se a carga for 0, o CR será 0
