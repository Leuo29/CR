class Aluno:
    def __init__(self, matricula: int):
        self._matricula = matricula
        self._matriculas = [] # Lista de objetos Matricula
        self._cr = 0.0 # CR inicializado

    @property
    def matricula(self) -> int:
        return self._matricula

    @property
    def cr(self) -> float:
        return self._cr
    
    def adicionar_matricula(self, matricula):
        self._matriculas.append(matricula)
