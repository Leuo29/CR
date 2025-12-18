from .matricula import Matricula
    ''' 
    classe criada apenas pra modelagem e para implementaçao futura
    na nossa aplicaçao nao tem uso ainda
    '''
class Aluno:
    def __init__(self, matricula: int):
        self._matricula = matricula
        self._matriculas = [] 
        self._cr = 0.0 

    @property
    def matricula(self) -> int:
        return self._matricula

    @property
    def cr(self) -> float:
        return self._cr
    
    def adicionar_matricula(self, matricula):
        self._matriculas.append(matricula)
