from flask import Flask, render_template, request
from consumer import listing_all, listing, search

app = Flask(__name__)

offset = 0

@app.route("/")
def index():
    characters = listing(offset)
    return render_template("index.html", characters = characters)

@app.route("/back", methods=["POST"])
def back():
    global offset
    if offset != 0:
        offset -= 20
    characters = listing(offset)
    return render_template("index.html", characters = characters)

@app.route("/advance", methods=["POST"])
def advance():
    global offset
    offset += 20
    characters = listing(offset)
    return render_template("index.html", characters = characters)

@app.route("/list_all", methods=["POST"])
def list_all():
    list_all = True
    characters = listing_all(0,0,[])
    return render_template("index.html", characters = characters, list_all = list_all)

@app.route("/search_for", methods=["POST"])
def search_for():
    searching = True
    name = request.form["character_name"]
    character = search(name)
    comics = character["comics"]
    return render_template("index.html", searching = searching, character = character, comics = comics)

app.run()
