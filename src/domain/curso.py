class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.matriculas = []

    def adicionar_matricula(self, matricula: Matricula):
        self.matriculas.append(matricula)

    def media_cr(self):
        total_cr = 0
        qtd = 0
        for matricula in self.matriculas:
            total_cr += matricula.cr
            qtd += 1
        if qtd > 0:
            return total_cr / qtd
        else:
            return 0.0
