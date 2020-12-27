from App import app
from flask import render_template
from jinja2 import Environment, PackageLoader
env_jinja = Environment(loader=PackageLoader('app_src', 'templates'))

@app.route('/')
@app.route('/questionnaire')
def questionnaire():
    return render_template(env_jinja.get_template('questionnaire.html'), title='Accueil')

@app.route('/favico.ico')
def favicon():
    return ''