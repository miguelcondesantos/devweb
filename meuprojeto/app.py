from flask import Flask, render_template

app = Flask("__name__")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")