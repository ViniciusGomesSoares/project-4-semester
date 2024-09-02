from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cupons = [
    {
     "imagem":"static/cupom-externo-combinou.png",
     "texto":"Combiniu deu match",
     "valor":"19,90"
    },
    {
     "imagem":"static/cupom-externo-heineken.png",
     "texto":"MINIBALDE = 2 HEINEKENS",
     "valor":"49,90"
    },
    {
     "imagem":"static/cupom-externob.png",
     "texto":"2 WRAPS CRUNCH + BATATA + REFRI",
     "valor":"27,90"
    },
    {
     "imagem":"static/cupom-externo-3S-2-wraps-batata-pequena-refri.png",
     "texto":"6 em 1: Crunch Jr + 1 Tira + Batata + Refri + Molho + Casquinha",
     "valor":"27,90"
    }
    ]
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
lista = [

]
@app.route("/")
def inicio():
    return render_template("inicio.html", cupom=cupons, cat=lista)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/form")
def formulario():
    return render_template("index.html")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)