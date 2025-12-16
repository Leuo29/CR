from .strategies.curso_cr_strategy import CursoCRStrategy

class Curso:

    def __init__(self, codigo: str): 
        self.codigo = codigo 
        self.nome = codigo    
        self.matriculas = []
        self.strategy = None 

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def media_cr(self, ano=None, semestre=None): 
        if not self.strategy:
            return 0.0

        return self.strategy.calcular_media(self, ano, semestre) 

    def __repr__(self):
        return f"Curso(codigo='{self.codigo}', total_matriculas={len(self.matriculas)})"