from flask import Flask, render_template
from consumer import listing

app = Flask(__name__)

characters = listing(0,0,[])

@app.route("/")
def index():
    return render_template("index.html", characters = characters)

app.run()
