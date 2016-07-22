from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    if request.method=="POST":
        user=request.form['nm']
    return render_template("resposta.html", name=user)

@app.route("/result")
def result():
    dict={'phy' : 50, 'che' : 60, 'maths' : 70}
    return render_template('table.html', result=dict)


if __name__ == '__main__':
    app.run(debug=True)
