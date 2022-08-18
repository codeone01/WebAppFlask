from app import app

from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h1 style='color: red'>About!!!</h1>"
