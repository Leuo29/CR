from .curso_cr_strategy import CursoCRStrategy

class CursoCRAlunoDisciplina(CursoCRStrategy):
    """
    Calcula a Média de CR do Curso considerando o CR GERAL de cada aluno 
    que cursou qualquer disciplina pertencente a este curso.
    """
    
    def __init__(self, todas_as_matriculas):
        # pega todas as matrículas disponíveis
        self.todas_as_matriculas = todas_as_matriculas

    def calcular_media(self, curso, ano=None, semestre=None):
        cr_somas = 0.0
        alunos_contados = set()  #para evitar contagem duplicada

        for matricula in self.todas_as_matriculas:
            
            if matricula.codigo in alunos_contados: #evita contar o aluno mais d uma vez
                continue
            
            # verifica se o aluno participou do curso em algum momento
            participou = False
            for nota in matricula.notas:
                # verifica se a disciplina pertence ao curso
                if nota.disciplina.curso is not None and nota.disciplina.curso.nome == curso.codigo:
                    participou = True 
                    break 
            # se participou e tem CR válido, soma o CR global
            if participou and matricula.cr > 0:
                cr_somas += matricula.cr
                alunos_contados.add(matricula.codigo)

        qtd_alunos = len(alunos_contados)

        if qtd_alunos > 0:
            return cr_somas / qtd_alunos
        else:
            return 0.0