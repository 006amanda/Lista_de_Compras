from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
itens = []
comprados = []

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

itens = []
comprados = []

@app.route("/")
def index():
    return render_template("index.html", itens=itens, comprados=comprados)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    itens.append(item)

    return render_template('partials/lista_comprar.html', itens=itens)

@app.route("/check/<int:id>")
def check(id):
    if 0 <= id < len(itens):
        item = itens.pop(id)
        comprados.append(item)
    return redirect(url_for("index"))

@app.route("/uncheck/<int:id>")
def uncheck(id):
    if 0 <= id < len(comprados):
        item = comprados.pop(id)
        itens.insert(0, item)
    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete():
    ids_itens = request.form.getlist("itens")
    ids_comprados = request.form.getlist("comprados")

    # remove itens normais
    for i in sorted([int(x) for x in ids_itens], reverse=True):
        if 0 <= i < len(itens):
            itens.pop(i)

    # remove itens comprados
    for i in sorted([int(x) for x in ids_comprados], reverse=True):
        if 0 <= i < len(comprados):
            comprados.pop(i)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)