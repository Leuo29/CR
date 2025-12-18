from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.views.decorators.http import require_GET
from io import StringIO

from .forms import UploadCRForm
from cr_logic.control.controller_dados import ControllerDados

"""
View principal da aplicação.
"""

class CRCalculatorView(View):
    
    template_name = 'home.html'

    def get(self, request):
        """
        - renderiza a home
        - o formulário de upload
        """
        estrategia_usada = request.session.get('estrategia_usada_na_sessao', 'disciplina')

        return render(request, self.template_name, {
            'form': UploadCRForm(),
            'results': None,
            'is_post': False,
            'estrategia_usada': estrategia_usada
        })

    def post(self, request):
        """
        - prepara o CSV para leitura
        - chama o controller
        """
        form = UploadCRForm(request.POST, request.FILES)
        results = {}
        file_object = None
        
        # estrategia escolhida para o calculo da media do curso
        estrategia = request.POST.get('estrategia', 'disciplina')

        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            ano = form.cleaned_data['ano'] or None
            semestre = form.cleaned_data['semestre'] or None

            
            session_data = request.session.get('processed_csv_content')

            if csv_file:
                try:
                    
                    csv_file.file.seek(0)
                    file_content = csv_file.file.read().decode('cp1252')
                except Exception as e:
                    results['error'] = f"Erro ao ler o arquivo: {e}"
                    return render(request, self.template_name, {
                        'form': form,
                        'results': results,
                        'is_post': True,
                        'estrategia_usada': estrategia
                    })

                # Salva o arquivo para reutilização
                request.session['processed_csv_content'] = file_content
                request.session['file_name'] = csv_file.name
                file_object = StringIO(file_content)

            elif session_data:
                # caso não seja feito upload, reutiliza o último CSV 
                file_object = StringIO(session_data)

            else:
                # nenhum arquivo nem historico
                results['error'] = "Por favor, selecione um arquivo CSV para começar o cálculo."
                return render(request, self.template_name, {
                    'form': form,
                    'results': results,
                    'is_post': True,
                    'estrategia_usada': estrategia
                })

            
            file_name_display = request.session.get('file_name', 'Dados da Sessão')

            try:
                # chama e cria o controller
                controller = ControllerDados(file_object)
                controller.processar_dados()

                # relatorios de CR e media
                cr_alunos = controller.get_cr_por_aluno_report()
                cr_cursos = controller.get_cr_por_curso_report(
                    ano=ano,
                    semestre=semestre,
                    estrategia=estrategia
                )

                results = {
                    'cr_alunos': cr_alunos,
                    'cr_cursos': cr_cursos,
                    'file_name': file_name_display,
                    'filters_used': {
                        'ano': ano,
                        'semestre': semestre,
                        'estrategia': estrategia
                    }
                }

                
                request.session['raw_data'] = self._extract_raw_data(controller)
                request.session['estrategia_usada_na_sessao'] = estrategia
                request.session.modified = True

            except Exception as e:
                request.session.pop('processed_csv_content', None)
                request.session.pop('file_name', None)
                results['error'] = (
                    "Erro no processamento. Por favor, tente novamente com um arquivo válido. "
                    f"Detalhe: {e}"
                )

        return render(request, self.template_name, {
            'form': form,
            'results': results,
            'is_post': True,
            'estrategia_usada': estrategia
        })

    def _extract_raw_data(self, controller):
        """
        Extrai os dados das matrículas
        """
        return [
            {
                'ID_ALUNO': str(m.codigo),
                'COD_CURSO': str(m.curso.codigo),
                'DISCIPLINA': n.disciplina.nome,
                'NOTA': n.valor,
                'CARGA_HORARIA': n.disciplina.carga_horaria,
                'ANO': n.disciplina.ano,
                'SEMESTRE': n.disciplina.semestre,
            }
            for m in controller.get_matriculas()
            for n in m.notas
        ]


@require_GET
def aluno_detail_view(request, aluno_id):
    """
    exibe as infos das notas de um aluno 
    """
    raw_data = request.session.get('raw_data')
    if not raw_data:
        raise Http404("Dados não encontrados.")

    detalhes = [d for d in raw_data if d['ID_ALUNO'] == str(aluno_id)]
    if not detalhes:
        raise Http404("Aluno não encontrado.")

    return render(request, 'aluno_detail.html', {
        'aluno_id': aluno_id,
        'detalhes': detalhes
    })


@require_GET
def curso_detail_view(request, curso_cod):
    """
    exibe as infos das disciplinas associadas a um curso
    """
    raw_data = request.session.get('raw_data')
    if not raw_data:
        raise Http404("Dados não encontrados.")

    detalhes = [d for d in raw_data if d['COD_CURSO'] == str(curso_cod)]
    if not detalhes:
        raise Http404("Curso não encontrado.")

    return render(request, 'curso_detail.html', {
        'curso_cod': curso_cod,
        'detalhes': detalhes
    })
