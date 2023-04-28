from flask import Flask, render_template
from consumer import listing_all, listing

app = Flask(__name__)

offset = 0

@app.route("/")
def index():
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
    characters = listing_all(0,0,[])
    return render_template("index.html", characters = characters)

@app.route("/search", methods=["POST"])
def search():
    return render_template("index.html")

app.run()
