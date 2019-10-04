from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inc():
    return render_template('investimentos.html', titulo = 'Investimentos')


app.run()