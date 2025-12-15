import pandas as pd

class LeitorCSV:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def ler_dados(self):
        # Lê o CSV em um DataFrame
        df = pd.read_csv(self.caminho_arquivo)
        # Converte para lista de dicionários, cada linha = um dict
        return df.to_dict(orient='records')
