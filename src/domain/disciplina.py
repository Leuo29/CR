
from .curso import Curso
class Disciplina:
    def __init__(self, codigo: str, nome: str, carga_horaria: int, curso=None):
        self.codigo = codigo
        self.nome = nome
        self.curso = curso  # novo atributo
        if carga_horaria >= 0:
            self.carga_horaria = carga_horaria
        else:
            print("carga horaria invalida, sera atribuido 0 no lugar")
            self.carga_horaria = 0
