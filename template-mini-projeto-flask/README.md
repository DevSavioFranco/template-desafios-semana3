# Mini-Projeto Flask

**Disciplinas:** LTP3 + QP3 (integradas)  
**Professor:** Rafael Martins Alves  
**CEMIC 2026**

---

## Objetivo

Criar uma aplicação web simples usando **Flask** que demonstre os conceitos aprendidos em aula: rotas, templates HTML, formulários e validação de dados.

## Escolha um tema

| # | Tema | Descrição |
|---|------|-----------|
| 1 | **Calculadora de IMC** | Formulário com peso/altura, calcula e classifica (abaixo do peso, normal, sobrepeso, obeso) |
| 2 | **Conversor de Moedas** | Input de valor + moeda origem/destino, converte entre Real, Dólar e Euro |
| 3 | **Lista de Tarefas** | Adicionar, listar e remover tarefas (armazenadas em memória/lista) |
| 4 | **Cadastro de Alunos** | Cadastrar nome + nota, listar todos, filtrar aprovados/reprovados |
| 5 | **Quiz de Python** | Perguntas sobre Python com alternativas, calcula pontuação final |

**Edite este README** e escreva abaixo qual tema você escolheu:

> **Tema escolhido:** (escreva aqui)

---

## Requisitos obrigatórios

1. **App funcional** — `python app.py` roda sem erro
2. **Pelo menos 2 rotas** — ex: `/` (página inicial) e `/resultado`
3. **Template HTML** — usar `render_template()` com pelo menos 1 arquivo `.html` na pasta `templates/`
4. **Formulário POST** — um formulário HTML que envia dados via POST e processa no Flask
5. **Validação** — validar entrada do usuário (try/except ou if/else)

## Estrutura do projeto

```
meu-projeto/
├── app.py                 ← Arquivo principal (EDITE ESTE)
├── requirements.txt       ← Dependências
├── templates/
│   └── index.html         ← Template base (EDITE ESTE)
├── static/
│   └── style.css          ← CSS opcional
├── tests/
│   └── test_app.py        ← Testes automáticos (NÃO EDITE)
├── .gitignore
└── README.md              ← Este arquivo
```

## Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar o app
python app.py

# Abrir no navegador
# http://127.0.0.1:5000
```

## Como entregar

```bash
git add .
git commit -m "meu mini-projeto flask"
git push
```

A correção automática roda a cada push. Veja o resultado na aba **Actions**.

## Critérios de Avaliação (100 pontos)

| Critério | Descrição | Pontos |
|----------|-----------|--------|
| App roda | `python app.py` funciona sem erro | 20 |
| Rotas | Pelo menos 2 rotas funcionais | 20 |
| Template HTML | Usa `render_template` com Jinja2 | 20 |
| Formulário | Formulário POST que processa dados | 20 |
| Validação | Valida entrada (try/except ou if/else) | 20 |

**Nota compartilhada LTP3 + QP3**
