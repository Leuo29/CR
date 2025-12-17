import pandas as pd

class LeitorCSV:
    
    def __init__(self, file_object): 
        self.file_object = file_object

    def ler_dados(self):
        # Lê o CSV diretamente do objeto de arquivo
        df = pd.read_csv(self.file_object)
        
        
        df['NOTA'] = pd.to_numeric(df['NOTA'], errors='coerce').fillna(0)
        df['CARGA_HORARIA'] = pd.to_numeric(df['CARGA_HORARIA'], errors='coerce').astype('Int64')
        df['MATRICULA'] = pd.to_numeric(df['MATRICULA'], errors='coerce').astype('Int64')
        
        # Retorna lista de dicionários
        return df.to_dict(orient='records')