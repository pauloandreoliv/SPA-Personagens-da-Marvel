from flask import Flask, render_template, request
from consumer import listing_all, listing, search

app = Flask(__name__)

offset = 0

@app.route("/")
def index():
    characters = listing(offset)
    character = {"name": "SEM PERSONAGEM", "description": "Procure algum personagem. Basta inserir o nome do(a) personagem desejado em Inglês. Ex: Captain America", "thumbnail": "https://i.imgur.com/QN8GUmf.jpg"}
    return render_template("index.html", characters = characters, character = character)


@app.route("/advance", methods=["POST"])
def advance():
    global offset
    offset += 20
    characters = listing(offset)
    return render_template("index.html", characters = characters)

@app.route("/list_all", methods=["POST"])
def list_all():
    characters = listing_all(0,0,[])
    return render_template("index.html", characters = characters)

@app.route("/search_for", methods=["POST"])
def search_for():
    name = request.form["character_name"]
    character = search(name)
    comics = character["comics"]
    return render_template("index.html", character = character, comics = comics)

app.run()
