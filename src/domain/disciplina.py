from .curso import Curso

class Disciplina:
    def __init__(self, codigo: str, nome: str, carga_horaria: int, ano: int, semestre: int, curso=None):
        self.codigo = codigo
        self.nome = nome
        self.curso = curso  
        self.ano = ano
        self.semestre = semestre
        
        if carga_horaria >= 0:
            self.carga_horaria = carga_horaria
        else:
            print(f"Carga horária inválida para {codigo}, será atribuído 0.")
            self.carga_horaria = 0

    def __repr__(self):
        return f"Disciplina(codigo='{self.codigo}', nome='{self.nome}', CH={self.carga_horaria}, Ano/Semestre={self.ano}/{self.semestre})"