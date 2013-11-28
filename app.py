from flask import Flask


app = Flask("wass")

@app.route("/")
def index():
	return "<h1>Yee mo'fucka!</h1>"


if __name__ == '__main__':
	app.run(debug=True)