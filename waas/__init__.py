from flask import Flask


app = Flask(__name__, static_folder='site')
import waas.views

# Change the jinja delimters so that they don't conflict with angular.
app.jinja_options = app.jinja_options.copy()
app.jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>',
))
