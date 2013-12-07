from flask import render_template

from waas import app


@app.route("/")
def index():
    return render_template('splash.html')
