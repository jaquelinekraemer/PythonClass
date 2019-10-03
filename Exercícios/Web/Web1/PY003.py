from flask import Flask, render_template, request, redirect
from alunos import Alunos
pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Jaqueline', 'Kraemer', 47998884455)
aluno2 = Alunos('Exemplo', 'Dois', 47991254871)
aluno3 = Alunos('Exemplo', 'Três', 47999815423)
aluno4 = Alunos('Exemplo', 'Quatro', 47991269893)

lista_alunos = [aluno1, aluno2, aluno3, aluno4]


app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos(nome, sobrenome, telefone)
    lista_alunos.append(novo_aluno)
    return redirect('/')
app.run()

#render_template??