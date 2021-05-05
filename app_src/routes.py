from App import app
from flask import render_template, redirect
from jinja2 import Environment, PackageLoader
from .forms.questionnaire_form import Generate_questionnaire
env_jinja = Environment(loader=PackageLoader('app_src', 'templates'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    form = Generate_questionnaire()
    form.subject.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.notion.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.level.choices = [(0, "Choix 0"), (1, "Choix 1")]
    form.difficulty.choices = [(0, "Choix 0"), (1, "Choix 1")]
    if form.validate_on_submit():
        # TODO
        redirect("/")
    return render_template(env_jinja.get_template('questionnaire.html'), form=form)

@app.route('/favico.ico')
def favicon():
    return ''