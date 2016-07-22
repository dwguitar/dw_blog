from flask import Flask, redirect, url_for, request
from flask import render_template
import os 

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
