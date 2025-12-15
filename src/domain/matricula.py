from .curso import Curso
from .nota import Nota

class Matricula:
    def __init__(self, codigo: str, curso: 'Curso'):
        self.codigo = codigo
        self.curso = curso
        self.notas = []
        self.cr = 0.0  # Inicializa o CR como 0.0

    def adicionar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_cr(self):
        total_ponderado = 0
        total_carga = 0
        for nota in self.notas:
            total_ponderado += nota.valor * nota.disciplina.carga_horaria
            total_carga += nota.disciplina.carga_horaria
        if total_carga > 0:
            self.cr = total_ponderado / total_carga
        else:
            self.cr = 0.0  # Se a carga for 0, o CR será 0
        return self.cr
