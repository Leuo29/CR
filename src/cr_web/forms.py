from django import forms

class UploadCRForm(forms.Form):
    """
    Formulário para arquivo CSV.
    Campos de filtro (ano/semestre) foram removidos e
    garantidos como vazios no cleaned_data.
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