from django import forms

class UploadCRForm(forms.Form):
    """
    Formulário responsável pelo upload do arquivo CSV
    OBS.: ja retorna os filtros sempre como nao filtrados
    para add filtros é so adicionar os campos pra informar ano e semestre
    foram removidos pq senti q n faziam sentido nesta implementaçao 
    """
    
    csv_file = forms.FileField(
        label='Selecione o arquivo CSV de notas',
        help_text='O arquivo deve conter as colunas necessárias.',
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()

        if 'ano' not in cleaned_data:
            cleaned_data['ano'] = ''

        if 'semestre' not in cleaned_data:
            cleaned_data['semestre'] = ''

        return cleaned_data
