from flask import Flask, render_template
from flask.globals import request
from script import run

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blend', methods=['GET', 'POST'])
def blend():
    req = request.form
    fat = req.get("fat")
    protien = req.get("protien")
    sugar = req.get("sugar")
    print(fat, protien, sugar)
    return render_template('animation.html', result=req)


@app.route('/result', methods=['GET', 'POST'])
def result():
    req = request.form
    fat = req.get("fat")
    protein = req.get("protien")
    sugar = req.get("sugar")
    response = run(fat, protein, sugar)
    return render_template('results.html', response=response)


if __name__ == "__main__":
    app.run()
