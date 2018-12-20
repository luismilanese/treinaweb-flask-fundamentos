from app import app

@app.route("/ola", defaults={'nome': None})
@app.route("/ola/<string:nome>")
def ola(nome):
    if nome:
        return f"Olá, {nome}"
    else:
        return "Olá, usuário"

@app.route("/oi")
def oi():
    return "Oi, mundo em Flask!!"