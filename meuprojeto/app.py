from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'fatec'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contatos", methods = ['POST', 'GET'])
def contatos():
    if request.method == 'POST':
        email = request.form['email']
        assunto =  request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contatos(email, assunto, descricao) values(%s, %s, %s)', (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
        return "sucesso"
    return render_template("contatos.html")

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM contatos")
    if users > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", userDetails=userDetails)


