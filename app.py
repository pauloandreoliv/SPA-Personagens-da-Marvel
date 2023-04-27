from flask import Flask, render_template
from consumer import listing

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run()
