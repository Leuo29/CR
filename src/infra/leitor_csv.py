import pandas as pd

   # Responsável pela leitura de arquivos CSV. Retorna os dados em formato estruturado 


class LeitorCSV:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def ler_dados(self):
        # Retorna um DataFrame do pandas
        return pd.read_csv(self.caminho_arquivo)
