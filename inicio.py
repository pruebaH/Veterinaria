from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/chaefresita')
def chaefresita():
    return render_template("chaefresita.html")

@app.route('/durazmomo')
def durazmomo():
    return render_template("durazmomo.html")

@app.route('/manzanayeon')
def manzanayeon():
    return render_template("manzanayeon.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")


@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(debug=True)
