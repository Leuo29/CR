from src.control.controller_dados import ControllerDados

# Instancia o ControllerDados com o arquivo CSV
controller = ControllerDados('notas.csv')

# Processa os dados do arquivo
controller.processar_dados()

# --- IMPRESSÃO DO CR POR ALUNO (EXISTENTE) ---

# Dicionário para armazenar os CRs de cada aluno
alunos_cr = {}

# Itera sobre as matrículas e adiciona o CR de cada matrícula no dicionário de alunos
for matricula in controller.get_matriculas():
    aluno_id = matricula.codigo  # Código do aluno (matrícula)
    if aluno_id not in alunos_cr:
        alunos_cr[aluno_id] = []  # Cria uma lista para armazenar os CRs do aluno
    alunos_cr[aluno_id].append(matricula.cr)  # Adiciona o CR da matrícula do aluno

print("### CR Médio por Aluno ###")
# Imprime o CR médio de cada aluno
for aluno, crs in alunos_cr.items():
    media_cr = sum(crs) / len(crs)  # Calcula a média dos CRs para o aluno
    print(f'Aluno: {aluno}, CR Médio: {media_cr:.2f}')


# --- NOVO: IMPRESSÃO DA MÉDIA DO CR POR CURSO ---

print("\n### Média do CR por Curso ###")
# Obtém o dicionário de cursos
cursos = controller.get_cursos() 

print("\n### Média do CR por Curso (Estratégia por Aluno) ###")
for codigo_curso in cursos:
    media_cr_aluno = controller.media_cr_por_aluno(codigo_curso)
    print(f'Curso: {codigo_curso}, Média do CR (por aluno): {media_cr_aluno:.2f}')

print("\n### Média do CR por Curso (Estratégia por Disciplina) ###")
for codigo_curso in cursos:
    media_cr_disciplina = controller.media_cr_por_disciplina(codigo_curso)
    print(f'Curso: {codigo_curso}, Média do CR (por disciplina): {media_cr_disciplina:.2f}')