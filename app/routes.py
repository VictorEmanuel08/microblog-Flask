from app import app
from flask import render_template

@app.route('/')
@app.route('/index', defaults={'nome':'usuário'})
@app.route('/index/<nome>/<profissao>/<stack>')
def index(nome, profissao, stack):
    dados = {"profissao": profissao, "stack": stack}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')