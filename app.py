from flask import Flask, render_template, redirect, request
import datamanager

app = Flask(__name__)


@app.route('/')
def index():
    # if request.form["drop"] == "asc by english":

    szotar = datamanager.list_words()
    return render_template("index.html", szotar=szotar)


@app.route('/hungarian-asc')
def hungarian_asc():
    szotar = datamanager.list_words_hungarian_asc()
    return render_template("hungarian_asc.html", szotar=szotar)


@app.route('/hungarian-desc')
def hungarian_desc():
    szotar = datamanager.list_words_hungarian_desc()
    return render_template("hungarian_desc.html", szotar=szotar)


@app.route('/english-asc')
def english_asc():
    szotar = datamanager.list_words_english_asc()
    return render_template("english_asc.html", szotar=szotar)


@app.route('/english-desc')
def english_desc():
    szotar = datamanager.list_words_hungarian_asc()
    return render_template("english_desc.html", szotar=szotar)



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
