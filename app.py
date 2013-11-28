from flask import Flask, render_template, redirect, url_for


app = Flask("wass", static_folder='site')

@app.route("/")
def index():
	return redirect(url_for('static', filename="index.html"))


if __name__ == '__main__':
	app.run(debug=True)