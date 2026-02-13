from flask import Flask, render_template, request
from random import choices

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run(host='0.0.0.0', port=81)