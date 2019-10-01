from flask import Flask, render_template
from alunos import Alunos
pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Jaqueline Kraemer', 47991117701)
aluno2 = Alunos('Catarina Lange', 47991254871)
lista_alunos = [aluno1, aluno2]
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)
app.run()