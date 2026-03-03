"""
Testes automáticos — Mini-Projeto Flask
LTP3 + QP3 — CEMIC 2026

Cada teste vale 20 pontos (5 testes x 20 = 100 pontos).
NÃO EDITE ESTE ARQUIVO.
"""

import os
import ast
import sys
import importlib

# Diretório raiz do projeto
DIRETORIO_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_app_roda():
    """
    Teste 1: O app.py importa sem erro (20 pontos)
    Verifica se o arquivo app.py existe e pode ser importado
    sem gerar exceções.
    """
    app_path = os.path.join(DIRETORIO_RAIZ, "app.py")

    # Arquivo existe?
    assert os.path.exists(app_path), \
        "Arquivo app.py não encontrado na raiz do projeto!"

    # Código Python válido?
    with open(app_path, "r", encoding="utf-8") as f:
        codigo = f.read()
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        raise AssertionError(
            f"app.py tem erro de sintaxe na linha {e.lineno}: {e.msg}"
        )

    # Importa sem erro?
    sys.path.insert(0, DIRETORIO_RAIZ)
    try:
        if "app" in sys.modules:
            del sys.modules["app"]
        mod = importlib.import_module("app")
        assert hasattr(mod, "app"), \
            "app.py não tem o objeto 'app'. Crie com: app = Flask(__name__)"
    except Exception as e:
        raise AssertionError(f"Erro ao importar app.py: {e}")
    finally:
        sys.path.pop(0)


def test_rotas():
    """
    Teste 2: Pelo menos 2 rotas definidas (20 pontos)
    Verifica se o app.py contém pelo menos 2 decoradores @app.route.
    """
    app_path = os.path.join(DIRETORIO_RAIZ, "app.py")
    assert os.path.exists(app_path), "Arquivo app.py não encontrado!"

    with open(app_path, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Contar ocorrências de @app.route
    import re
    rotas = re.findall(r"@app\.route\(", codigo)
    assert len(rotas) >= 2, \
        f"Encontradas apenas {len(rotas)} rota(s). Você precisa de pelo menos 2 rotas (@app.route)."


def test_template():
    """
    Teste 3: Usa render_template com arquivo HTML (20 pontos)
    Verifica se app.py usa render_template e se existe pelo menos
    1 arquivo .html na pasta templates/.
    """
    app_path = os.path.join(DIRETORIO_RAIZ, "app.py")
    templates_dir = os.path.join(DIRETORIO_RAIZ, "templates")

    assert os.path.exists(app_path), "Arquivo app.py não encontrado!"

    with open(app_path, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Usa render_template?
    assert "render_template" in codigo, \
        "app.py não usa render_template(). Importe e use para renderizar HTML."

    # Pasta templates existe?
    assert os.path.isdir(templates_dir), \
        "Pasta templates/ não encontrada. Crie a pasta e adicione seus arquivos .html."

    # Tem pelo menos 1 arquivo .html?
    html_files = [f for f in os.listdir(templates_dir) if f.endswith(".html")]
    assert len(html_files) >= 1, \
        "Nenhum arquivo .html encontrado em templates/. Crie pelo menos 1 template."

    # O HTML não está vazio?
    for html_file in html_files:
        html_path = os.path.join(templates_dir, html_file)
        with open(html_path, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
        assert len(conteudo) > 50, \
            f"O arquivo templates/{html_file} parece vazio ou muito curto. Implemente seu template."


def test_formulario():
    """
    Teste 4: Formulário POST funcional (20 pontos)
    Verifica se existe um formulário com method="POST" no HTML
    e se o app.py processa requisições POST.
    """
    app_path = os.path.join(DIRETORIO_RAIZ, "app.py")
    templates_dir = os.path.join(DIRETORIO_RAIZ, "templates")

    assert os.path.exists(app_path), "Arquivo app.py não encontrado!"

    with open(app_path, "r", encoding="utf-8") as f:
        codigo_py = f.read()

    # app.py aceita POST?
    assert "POST" in codigo_py, \
        'app.py não processa POST. Adicione methods=["POST"] em alguma rota.'

    # app.py usa request.form?
    assert "request.form" in codigo_py or "request.get_json" in codigo_py, \
        "app.py não lê dados do formulário. Use request.form[\"campo\"] para ler os dados."

    # HTML tem formulário com POST?
    if os.path.isdir(templates_dir):
        html_files = [f for f in os.listdir(templates_dir) if f.endswith(".html")]
        tem_form_post = False
        for html_file in html_files:
            html_path = os.path.join(templates_dir, html_file)
            with open(html_path, "r", encoding="utf-8") as f:
                conteudo = f.read().lower()
            if "method=" in conteudo and "post" in conteudo and "<form" in conteudo:
                tem_form_post = True
                break
        assert tem_form_post, \
            'Nenhum template tem <form method="POST">. Adicione um formulário.'


def test_validacao():
    """
    Teste 5: Validação de dados (20 pontos)
    Verifica se app.py contém validação de entrada do usuário
    usando try/except ou verificações com if.
    """
    app_path = os.path.join(DIRETORIO_RAIZ, "app.py")
    assert os.path.exists(app_path), "Arquivo app.py não encontrado!"

    with open(app_path, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Remove comentários e docstrings para análise mais precisa
    linhas = codigo.split("\n")
    linhas_codigo = [
        l for l in linhas
        if l.strip() and not l.strip().startswith("#")
    ]
    codigo_limpo = "\n".join(linhas_codigo)

    # Verifica se tem try/except OU validação com if
    tem_try = "try:" in codigo_limpo and "except" in codigo_limpo
    tem_validacao_if = False

    # Padrões comuns de validação
    padroes_validacao = [
        "if not", "if len(", ".isdigit()", ".isnumeric()",
        "ValueError", "KeyError", "TypeError",
        "if request.form", "is None", "== ''", '== ""',
        "strip()", ".isalpha()", "if erro", "if not campo",
    ]

    for padrao in padroes_validacao:
        if padrao in codigo_limpo:
            tem_validacao_if = True
            break

    assert tem_try or tem_validacao_if, \
        "app.py não contém validação de dados. Use try/except ou if para validar a entrada do usuário."
