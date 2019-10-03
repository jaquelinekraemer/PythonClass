from flask import Flask, render_template, request, redirect
from cadastro import Cerveja

app=Flask(__name__)
lista_cervejas = []
lista_pedidos = []

@app.route('/')
def inc():
    return render_template('tbl.html', titulo_pagina = 'Titulo')

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_pagina = 'Listar', lista=lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_pagina = 'Cadastrar')

@app.route('/fazerpedido')
def fazerpedido():
    return render_template('fazerpedido.html', titulo_pagina = 'Fazer Pedido')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    preco = request.form['preco']
    validade = request.form['validade']
    nova_cerveja = Cerveja(nome, tipo, preco, validade)
    lista_cervejas.append(nova_cerveja)
    return redirect ('/listar')

@app.route('/salvarpedido', methods=['POST'])
def salvarpedido():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    nova_lista = Cerveja(nome, quantidade)
    lista_pedidos.append(nova_lista)
    return redirect ('/salvarpedido')

app.run()