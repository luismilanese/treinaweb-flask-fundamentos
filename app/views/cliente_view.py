from app import app

@app.route("/ola")
def ola():
    return "Olá, mundo em Flask!!"

@app.route("/oi")
def oi():
    return "Oi, mundo em Flask!!"