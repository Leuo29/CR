class Nota:
    def __init__(self, disciplina: Disciplina, valor: float):
        self.disciplina = disciplina
        if valor >=0 and valor <= 100:
            self.valor = valor            
        else:
            print("valor inserido invalido, sera colocado como 0")
            self.valor = 0