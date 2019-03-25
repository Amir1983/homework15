from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def hello():
    zahl = int(request.args.get("zahl","0"))

    return render_template("index.html", zahl=zahl,  glueckszahl = random.randint(1, 10))

@app.route("/Dateneingabe", methods=["GET", "POST"])
def test():
    name = request.form.get("name")
    nachname = request.form.get("nachname")
    adresse = request.form.get("adresse")

    print(name)
    print(nachname)
    print(adresse)
    return render_template("startseite.html")
if __name__ =='__main__':
    app.run(debug=True)

