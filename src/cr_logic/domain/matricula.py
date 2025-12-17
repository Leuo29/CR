from .curso import Curso
from .nota import Nota

class Matricula:
    def __init__(self, codigo: str, curso: 'Curso'):
        self.codigo = codigo
        self.curso = curso
        self.notas = []
        self.cr = 0.0  

    def adicionar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_cr(self):
        """
        Calcula o CR ponderado pelas cargas horárias das disciplinas.
        Retorna 0.0 se não houver notas.
        somatorio( Notas * cargas)/somatorio(cargas) 
        """
        somatorio_nota_carga = 0
        somatorio_carga = 0

        #realiza o somatorio
        for nota in self.notas:
            somatorio_nota_carga += nota.valor * nota.disciplina.carga_horaria
            somatorio_carga += nota.disciplina.carga_horaria
        #realiza a divisao ou 0 em casos de carga zerada, evitando divisao por 0
        if somatorio_carga > 0:
            self.cr = somatorio_nota_carga / somatorio_carga
        else:
            self.cr = 0.0  # Se a carga for 0, o CR será 0
        return self.cr
