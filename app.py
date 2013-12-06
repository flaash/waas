from flask import Flask, render_template, redirect, url_for


app = Flask("wass", static_folder='site')
#Change the jinja delimters so that they don't conflict with angular.
app.jinja_options = app.jinja_options.copy()
app.jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

@app.route("/")
def index():
	return render_template('splash.html')
	#return redirect(url_for('static', filename="splash.html"))


if __name__ == '__main__':
	app.run(debug=True)