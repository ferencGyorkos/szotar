from flask import Flask, render_template, redirect, request
import datamanager

app = Flask(__name__)


@app.route('/')
def index():
    szotar = datamanager.list_words()
    return render_template("index.html", szotar=szotar)


@app.route('/add-word', methods=["POST", "GET"])
def add_word():
    if request.method == 'POST':
        szotarpost = request.form.to_dict()
        print(szotarpost)
        datamanager.new_word(szotarpost['magyar'], szotarpost['angol'])
        return redirect("/")
    else:
        return render_template("add_word.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
