"""
Mini-Projeto Flask — LTP3 + QP3
CEMIC 2026 — Prof. Rafael Martins Alves

INSTRUÇÕES:
1. Escolha seu tema (veja o README.md)
2. Edite este arquivo com suas rotas e lógica
3. Crie/edite os templates HTML na pasta templates/
4. Teste rodando: python app.py
5. Faça git add, commit e push para entregar

REQUISITOS:
- Pelo menos 2 rotas
- Usar render_template() com arquivo .html
- Formulário com method="POST"
- Validação de dados (try/except ou if/else)
"""

from flask import Flask, render_template, request

app = Flask(__name__)


# ============================================
# ROTA 1: Página inicial
# ============================================
@app.route("/")
def inicio():
    return render_template("index.html")


# ============================================
# ROTA 2: Processamento do formulário
# Exemplo: Calculadora de IMC
# Adapte para o seu tema escolhido!
# ============================================
@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        # TODO: Substitua este exemplo pela lógica do seu tema
        # Exemplo para IMC:
        # peso = float(request.form["peso"])
        # altura = float(request.form["altura"])
        # imc = peso / (altura ** 2)
        # return render_template("index.html", resultado=f"Seu IMC: {imc:.1f}")

        # Por enquanto retorna a página inicial
        return render_template("index.html", resultado="Implemente sua lógica aqui!")

    except (ValueError, KeyError):
        return render_template("index.html", erro="Dados inválidos! Tente novamente.")


# ============================================
# NÃO MODIFIQUE ABAIXO
# ============================================
if __name__ == "__main__":
    app.run(debug=True)
