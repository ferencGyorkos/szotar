from flask import Flask, render_template, redirect, request
import datamanager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add-word')
def add_word():
    if request.method == 'POST':
        szotarpost = request.form.to_dict()
        print(szotarpost)
        datamanager.new_word(szotarpost['magyar'], szotarpost['angol'])
        return render_template('index.html')
    else:
        return render_template("add_word.html")


if __name__ == '__main__':
    app.run(port=5200, debug=True)
