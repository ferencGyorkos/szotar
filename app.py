from flask import Flask, render_template, redirect, request
import datamanager

app = Flask(__name__)


@app.route('/')
def index():
    szotar = datamanager.list_words()
    return render_template('index.html', szotar=szotar)


@app.route('/<order>')
def order_by(order):
    szotar = None
    if order == 'hungarian-asc':
        szotar = datamanager.list_words_hungarian_asc()
    elif order == 'hungarian-desc':
        szotar = datamanager.list_words_hungarian_desc()
    elif order == 'english-asc':
        szotar = datamanager.list_words_english_asc()
    elif order == 'english-desc':
        szotar = datamanager.list_words_english_desc()
    elif order == 'delete-word':
        id = request.form['id']
        datamanager.delete_word_by_id(id)
    return render_template("index.html", szotar=szotar)

@app.route('/delete-word')
def delete_by_id():
    id = request.form['id']
    datamanager.delete_word_by_id()
    return redirect('/')


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
