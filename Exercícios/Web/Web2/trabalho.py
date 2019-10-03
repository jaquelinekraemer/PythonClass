from flask import Flask, render_template

app = Flask(__name__) #executando o flask
@app.route('/') #cria a rota
def inicio(): #função para definir método
    return render_template('index.html')
app.run()