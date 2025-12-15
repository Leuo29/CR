from .strategies.curso_cr_strategy import CursoCRStrategy

class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.matriculas = []

    def adicionar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def media_cr(self):
        if not self.strategy:
            return 0.0
        return self.strategy.calcular_media(self)
