import pandas as pd

class LeitorCSV:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def ler_dados(self):
 
        df = pd.read_csv(self.caminho_arquivo)
       
        return df.to_dict(orient='records')
