# Desafio 3 – Cálculo de CR (Coeficiente de Rendimento)

Este projeto foi desenvolvido como solução para o Desafio 3 do processo seletivo de estágio do STI/UFF. O objetivo é calcular o Coeficiente de Rendimento (CR) dos alunos a partir de um arquivo CSV e apresentar as médias de CR por curso.

## Como baixar e rodar o projeto

Siga os passos abaixo. Você não precisa ter nada instalado previamente além do Python e se quiser o Git segue tutorialzinho de como instalar:

```
https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git
```
Obs.: Alternativamente basta baixar o zip do projeto e seguir pro passo 2
### 1. Clonar o projeto

Abra o seu terminal (CMD/PowerShell no Windows ou Terminal no Linux/WSL) e digite:

```bash
git clone https://github.com/Leuo29/CR.git
cd CR
```

### 2. Criar e ativar o ambiente virtual

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / Ubuntu / WSL

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os testes automatizados

Antes de rodar a interface, é importante validar se os cálculos estão corretos:

```bash
python -m pytest src/cr_logic/tests
```

### 5. Rodar a interface web (Django)

```bash
# Entre na pasta do projeto Django
cd src

# Prepare o banco de dados inicial (executar apenas na primeira vez)
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Agora, abra o navegador e acesse:

```
http://127.0.0.1:8000
```
Pronto! Está funcionando =)

---

## Sobre o Projeto

O sistema recebe um arquivo CSV contendo notas de alunos e gera o calculo dos CRs destes alunos e a media de CRs por curso. O foco do desenvolvimento foi em Orientação a Objetos, tentando manter ao maximo padroes de projeto Grasp e Gof (Aprendidos em proj. de software I)
Foi escolhido o python dada a sua simplicidade, e pelo costume de uso, assim como o framework Web Django, que tem facil instalaçao e utilizaçao


### Entrada de Dados

O sistema processa o arquivo no formato:

```
MATRICULA,COD_DISCIPLINA,COD_CURSO,NOTA,CARGA_HORARIA,ANO_SEMESTRE
```

### Regras

* A nota varia de 0 a 100.
* O CR individual do aluno é calculado como uma média ponderada pelas cargas horárias das disciplinas cursadas, definida pela seguinte fórmula:

```
CR = Σ(Nota_i × CargaHoraria_i) / Σ(CargaHoraria_i)
```

### Modelagem
O projeto foi desenvolvido em duas etapas, a produçao da logica (disponivel na pasta cr_logic) e a parte Web (o restante do projeto)
Na primeira etapa foram feitas as modelagens das classes que iriam ser usadas na interface, as classes e metodos. Após a modelagem inicial foi feito o projeto django vizando apenas usufruir a logica criada (logicamente algumas alterações foram feitas durante essa etapa tanto para refino da logica quando para melhor integração e funcionamento)
Foram criadas as Issues para delimitar as etapas e tarefas necessarias para a produção do projeto

Durante o projeto foram modelados as seguintes classes:

* **ControllerDados**: atua como maestro do sistema. É responsável por coordenar a leitura do CSV, acionar o gerenciador de entidades, manter as coleções de cursos e matrículas e delegar a geração de relatórios de CR por aluno e por curso
* **GerenciadorEntidades**: cria e relaciona as entidades de domínio (Curso, Disciplina, Matricula, Nota e Aluno) a partir dos dados fornecidos pelo LeitorCSV
* **LeitorCSV**: responsável pela leitura do arquivo CSV e pela conversão das linhas em estruturas de dados intermediárias, preparando as informações para o restante do codigo
* **RelatorioAlunoService**: calcula e organiza o CR individual de cada aluno a partir de suas matrículas
* **RelatorioCursoService**: centraliza o cálculo de media de CR dos cursos, aplicando dinamicamente a estratégia escolhida (por aluno, por disciplina ou por aluno-disciplina) listando os resultados. Obs.: Será explicado mais tarde o motivo de uso de estrategias


* **Aluno**: representa o aluno e mantém seu CR global, além da lista de matrículas associadas.
* **Curso**: representa um curso de graduação, agregando matrículas e delegando o cálculo do CR para uma estratégia configurada.
* **Disciplina**: representa uma disciplina pertencente a um curso, contendo informações como carga horária, ano e semestre.
* **Matricula**: representa o vínculo do aluno com um curso e suas disciplinas, armazenando notas e sendo responsável pelo cálculo do CR individual.
* **Nota**: encapsula o valor da nota obtida pelo aluno em uma disciplina específica.

O projeto utiliza o padrão **Strategy** para calcular a média dos cursos de três formas diferentes, isso pq a forma principal de calcular uma media de CRs d um curso seria fazendo uma media simples de todos os alunos do curso.
Porém ao verificar o padrao de entrada do arquivo exemplo diversas linhas tinham os mesmos alunos e cod de cursos diferentes, portanto curso aqui deve-se referir ao curso do qual a disciplina pertence.
Assim não tendo a estrategia tipica eu criei três estrategias de calculo desse CR medio:

* **Média ponderada por disciplina (CursoCRPorDisciplina)**: considera todas as disciplinas pertencentes ao curso, com peso por carga horária igual com o CR do aluno
```
Σ(Nota_i × CargaHoraria_i) / Σ(CargaHoraria_i)
```
* **Média simples dos CRs dos alunos (CursoCRPorAluno)**: cada aluno associado ao curso contribui com seu CR global. O sistema atribuiu o curso de aluno de acordo com a primeira linha q ele aparece
* **Média simples do CR dos alunos que cursaram alguma disciplina do curso (CursoCRAlunoDisciplina)**: se o aluno cursou ao menos uma disciplina do curso, seu CR global entra na média

Assim, usando o padrão strategy do padraão de modelagem Gof foram criadas as seguintes classes:

* **CursoCRStrategy**: classe abstrata que define o cálculo a media dos cursos.
* **CursoCRPorAluno**: calcula o CR do curso como a média simples dos CRs globais dos alunos associados.
* **CursoCRPorDisciplina**: calcula o CR do curso considerando todas as disciplinas pertencentes ao curso, com média ponderada por carga horária
* **CursoCRAlunoDisciplina**: calcula o CR do curso considerando o CR global dos alunos que cursaram ao menos uma disciplina do curso.


### Testes

Foi utilizado o framework **Pytest** para implementar testes, os seguintes testes foram feitos:

* Cálculo de CR: validação da conta e divisão por zero.
* Gerenciador de Entidades: verificação da criação correta de objetos a partir do CSV.
* Strategies: validação de cada cálculo de media de cr de curso.

---
Desenvolvido por Leonardo Sobrinho (Leuo29) 
